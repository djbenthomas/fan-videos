#!/usr/bin/env python3
"""Render 'operated camera' versions of the EPK clips.

Adds a slow push-in, deliberate punch-ins and a little handheld drift so the
footage reads as a person filming rather than a locked-off tripod.

usage: make_motion_clips.py [name ...]
"""
import os, subprocess, sys

SRC = os.path.expanduser('~/Movies/Fan Uploads')
OUT = os.path.expanduser('~/.openclaw/workspace-dale/fan-videos/epk/media')
FPS = 30

# name, source file, out size, duration s, punch frames, zoom rate, sway
CLIPS = [
    # fiddle showcase — three decisive punch-ins
    ('devil-georgia.mp4', 'Devil Went Down to Georgia 11-17-26.mov', (1280, 720), 187.8,
     [0.12, 0.46, 0.78], 0.10, 0.055),
    # singalong — slow push, one punch on the chorus
    ('cowboy.mp4', "Should've Been a Cowboy 11-17-26.mov", (1280, 720), 84.3,
     [0.34, 0.72], 0.08, 0.05),
    # vertical social cut — quicker, snappier
    ('surfin-usa-country.mp4', 'Surfin USA (Country Version) - IG Cut 60s.mp4', (720, 1280), 60.0,
     [0.18, 0.52, 0.80], 0.12, 0.06),
    # long set excerpt — gentle, watchable drift only
    ('lower-broadway-set.mp4', 'ZPierre Broadway Live 11-17-26 - Set 3.07-3.15.mp4', (854, 480), 480.0,
     [0.30, 0.68], 0.05, 0.035),
]


def step(on, start, ramp=7):
    """Quick eased-in jump that then holds (a zoom the operator snapped in)."""
    p = f'(on-{start})/{ramp}'
    return f'if(lt(on,{start}),0,if(lt(on,{start+ramp}),({p})*({p})*(3-2*({p})),1))'


def zoom_expr(n, punches, rate):
    z = f'(1.04+{rate:.3f}*on/{n})'
    deltas = [0.11, 0.09, 0.07]
    for i, f in enumerate(punches):
        z += f'+{deltas[i % 3]:.3f}*' + step(None, round(f * n))
    return f"min({z},1.42)"


def sway_expr(n, amp):
    # slow lateral sway + a faster, smaller vertical bob = handheld feel
    x = f'iw/2-(iw/zoom/2)+{amp:.4f}*iw*sin(on/{max(n//26,60)})'
    y = f'ih/2-(ih/zoom/2)+{amp*0.72:.4f}*ih*sin(on/{max(n//41,40)}+1.7)'
    return x, y


def render(name, src, size, dur, punches, rate, amp):
    n = int(dur * FPS)
    z = zoom_expr(n, punches, rate)
    x, y = sway_expr(n, amp)
    vf = (f"zoompan=z='{z}':x='{x}':y='{y}':d=1:s={size[0]}x{size[1]}:fps={FPS},"
          f"format=yuv420p")
    tmp = os.path.join(OUT, '.tmp-' + name)
    cmd = ['ffmpeg', '-y', '-v', 'error', '-i', os.path.join(SRC, src),
           '-vf', vf, '-c:v', 'libx264', '-crf', '25', '-preset', 'veryfast',
           '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
           '-c:a', 'aac', '-b:a', '128k', '-shortest', tmp]
    print('render', name, flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print('FAIL', name, r.stderr[-800:], flush=True)
        return False
    os.replace(tmp, os.path.join(OUT, name))
    print('OK', name, os.path.getsize(os.path.join(OUT, name)), flush=True)
    return True


if __name__ == '__main__':
    want = set(sys.argv[1:])
    for c in CLIPS:
        if want and c[0] not in want:
            continue
        render(*c)
