#!/usr/bin/env python3
"""Build the private live-reel page from setlist.json."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
songs = json.load(open(os.path.join(HERE, 'setlist.json')))

rows = '\n'.join(
    f'      <li><b>{t}</b><span>{a}</span></li>' for t, a in songs)

HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>You Can Have a Nashville Broadway Band Right in Your Backyard — Friends with Benny's</title>
<style>
  :root{{ --ink:#0e0e10; --paper:#f6f3ec; --gold:#c9a227; --muted:#9b9689; }}
  *{{box-sizing:border-box}}
  html,body{{margin:0;padding:0}}
  body{{background:var(--ink);color:var(--paper);font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}}
  a{{color:var(--gold);text-decoration:none}} a:hover{{text-decoration:underline}}
  .wrap{{max-width:1080px;margin:0 auto;padding:0 20px 80px}}
  header{{padding:62px 0 26px;border-bottom:1px solid #26262b}}
  .kicker{{font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:var(--gold)}}
  h1{{font-family:Georgia,"Times New Roman",serif;font-weight:400;font-size:46px;line-height:1.08;margin:14px 0 10px;letter-spacing:-.02em}}
  h1 em{{font-style:italic;color:var(--gold)}}
  .sub{{color:var(--muted);font-size:15px;max-width:660px}}
  .badge{{display:inline-block;margin-top:16px;border:1px solid #35353c;border-radius:999px;padding:6px 14px;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#cfcabb}}
  .stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:#26262b;margin:32px 0 8px;border:1px solid #26262b}}
  .stat{{background:#141417;padding:18px 16px}}
  .stat b{{display:block;font-family:Georgia,serif;font-size:26px;font-weight:400}}
  .stat span{{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}}
  h2{{font-family:Georgia,serif;font-weight:400;font-size:29px;margin:48px 0 6px;letter-spacing:-.01em}}
  h2 .thin{{color:var(--gold);font-style:italic}}
  .lede{{color:var(--muted);font-size:14.5px;margin:0 0 20px;max-width:740px}}
  .reel{{display:grid;grid-template-columns:1fr 1fr;gap:22px}}
  .card{{background:#151518;border:1px solid #26262b;border-radius:6px;overflow:hidden}}
  .card video{{display:block;width:100%;height:auto;background:#000}}
  .card .meta{{padding:14px 16px 16px}}
  .card h3{{font-family:Georgia,serif;font-weight:400;font-size:19px;margin:0 0 2px}}
  .card p{{margin:0;font-size:13px;color:var(--muted)}}
  .tag{{display:inline-block;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:6px}}
  .vert video{{max-height:560px;object-fit:contain;background:#000}}
  .cols{{display:grid;grid-template-columns:1fr 1fr;gap:34px;margin-top:8px}}
  ul.clean{{list-style:none;margin:0;padding:0}}
  ul.clean li{{padding:7px 0;border-bottom:1px solid #222227;font-size:14.5px}}
  ul.clean li b{{color:var(--paper);font-weight:600}}
  ul.setlist{{list-style:none;margin:10px 0 0;padding:0;column-count:3;column-gap:26px;font-size:12.5px;line-height:1.45}}
  ul.setlist li{{padding:2.5px 0;border-bottom:1px solid #1e1e22;break-inside:avoid;display:flex;justify-content:space-between;gap:8px}}
  ul.setlist li b{{font-weight:600;color:#ece7db}}
  ul.setlist li span{{color:#8d8879;font-size:11px;text-align:right;white-space:nowrap}}
  .quote{{border-left:3px solid var(--gold);padding:4px 0 4px 16px;margin:18px 0;font-family:Georgia,serif;font-style:italic;font-size:16.5px;color:#e6e1d6}}
  .quote small{{display:block;font-family:-apple-system,sans-serif;font-style:normal;font-size:12px;color:var(--muted);margin-top:6px}}
  .links{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px}}
  .link{{display:flex;justify-content:space-between;align-items:center;gap:12px;background:#151518;border:1px solid #26262b;border-radius:6px;padding:12px 14px;font-size:14px}}
  .link span{{color:var(--paper)}}
  .link em{{font-style:normal;color:var(--gold);font-size:12px;white-space:nowrap}}
  .pull{{font-family:Georgia,serif;font-style:italic;font-size:19px;line-height:1.45;border-left:3px solid #f6f3ec;padding-left:16px;margin:26px 0;color:#efeade}}
  footer{{margin-top:60px;padding-top:22px;border-top:1px solid #26262b;display:flex;justify-content:space-between;gap:20px;font-size:13px;color:var(--muted);flex-wrap:wrap}}
  @media (max-width:900px){{ul.setlist{{column-count:2}}}}
  @media (max-width:760px){{
    h1{{font-size:34px}}
    .stats{{grid-template-columns:1fr 1fr}}
    .reel{{grid-template-columns:1fr}}
    .cols{{grid-template-columns:1fr}}
    .links{{grid-template-columns:1fr}}
    ul.setlist{{column-count:1}}
    header{{padding-top:44px}}
  }}
</style>
</head>
<body>
<div class="wrap">

<header>
  <div class="kicker">Friends with Benny's &nbsp;·&nbsp; Nashville, Tennessee</div>
  <h1>You Can Have a Nashville<br>Broadway Band <em>Right in Your Backyard</em></h1>
  <p class="sub">Live performance reel — four clips shot this week on Lower Broadway. No tracks, no click, no studio
  edits. What you hear is the room.</p>
  <div class="badge">Private link · Chaparral Country Club · Entertainment Committee</div>

  <div class="stats">
    <div class="stat"><b>900+</b><span>Events played</span></div>
    <div class="stat"><b>5 nights</b><span>Per week on Broadway</span></div>
    <div class="stat"><b>{len(songs)}</b><span>Songs in the book</span></div>
    <div class="stat"><b>15+ yrs</b><span>Entertaining rooms</span></div>
  </div>
</header>

<h2>Watch the band <span class="thin">— four clips, newest first</span></h2>
<p class="lede">All four were shot in the last week on Lower Broadway. Sound is the room, not a mix — that's the point.</p>

<div class="reel">

  <div class="card">
    <video controls preload="none" playsinline poster="media/poster-devil.jpg">
      <source src="media/devil-georgia.mp4" type="video/mp4">
      Your browser doesn't support embedded video. <a href="media/devil-georgia.mp4">Download the clip</a>.
    </video>
    <div class="meta">
      <div class="tag">Fiddle showcase · 3:08</div>
      <h3>The Devil Went Down to Georgia</h3>
      <p>Full band, live. The one that tells you what the players can do.</p>
    </div>
  </div>

  <div class="card">
    <video controls preload="none" playsinline poster="media/poster-cowboy.jpg">
      <source src="media/cowboy.mp4" type="video/mp4">
      Your browser doesn't support embedded video. <a href="media/cowboy.mp4">Download the clip</a>.
    </video>
    <div class="meta">
      <div class="tag">Crowd singalong · 1:24</div>
      <h3>Should've Been a Cowboy</h3>
      <p>Toby Keith. This is the sound of a room that already knows every word.</p>
    </div>
  </div>

  <div class="card vert">
    <video controls preload="none" playsinline poster="media/poster-surfin.jpg">
      <source src="media/surfin-usa-country.mp4" type="video/mp4">
      Your browser doesn't support embedded video. <a href="media/surfin-usa-country.mp4">Download the clip</a>.
    </video>
    <div class="meta">
      <div class="tag">Country arrangement · 1:00</div>
      <h3>Surfin' USA — country version</h3>
      <p>Shot vertical for social. Shows the genre-bending side of the set.</p>
    </div>
  </div>

  <div class="card">
    <video controls preload="none" playsinline poster="media/poster-set.jpg">
      <source src="media/lower-broadway-set.mp4" type="video/mp4">
      Your browser doesn't support embedded video. <a href="media/lower-broadway-set.mp4">Download the set</a>.
    </video>
    <div class="meta">
      <div class="tag">Full set excerpt · 8:00</div>
      <h3>Lower Broadway, Nashville — 11/17/26</h3>
      <p>Eight unedited minutes from a working Broadway night. Real room, real crowd.</p>
    </div>
  </div>

</div>

<h2>On YouTube <span class="thin">— public links, if you'd rather share</span></h2>
<div class="links">
  <a class="link" href="https://youtu.be/qHdIGfxuXwQ" target="_blank" rel="noopener"><span>The Devil Went Down to Georgia — live</span><em>Watch ▸</em></a>
  <a class="link" href="https://youtu.be/hra35fpSrMM" target="_blank" rel="noopener"><span>Lower Broadway full set — 11/17/26</span><em>Watch ▸</em></a>
  <a class="link" href="https://youtu.be/X2CIsSlsncM" target="_blank" rel="noopener"><span>Dixieland Delight — Alabama cover, live</span><em>Watch ▸</em></a>
  <a class="link" href="https://www.youtube.com/@bennythomasband695" target="_blank" rel="noopener"><span>Full channel — new footage weekly</span><em>Open ▸</em></a>
</div>

<h2>Why a Nashville band is a different animal</h2>
<div class="cols">
  <div>
    <p style="margin-top:0;font-size:14.5px">Nashville's first-call players have been called the <b>"A-Team"</b> since the late
    1950s — a small circle of musicians who worked several sessions a day, for different artists and labels, and
    shaped the sound of the records everybody knows. The bar that built that reputation is still the bar in this
    town: players who <em>"read an arrangement quickly, adapt on the fly, and deliver a usable take in only a few
    tries."</em></p>
    <p class="lede" style="font-size:12.5px;margin-top:-10px">— The Little Nashville Opry, on Nashville's session players</p>
    <p style="font-size:14.5px">Lower Broadway is where that standard gets tested in public — four-hour sets, five
    nights a week, no rehearsal, a crowd two feet from the stage that has heard every one of these songs a hundred
    times. A band that survives that room can walk into any room.</p>
  </div>
  <div>
    <ul class="clean">
      <li><b>Three hours of live music</b> — two sets with a break, or continuous if the room is moving</li>
      <li><b>Set list built around the membership</b> — Merle and Hank to current country, plus the classic rock everybody actually dances to</li>
      <li><b>Dress and demeanor to club standard</b> — this is a country club, not a honky tonk</li>
      <li><b>Sound check in the afternoon</b>, off the dance floor before guests arrive</li>
      <li><b>Requests welcome</b> and usually played</li>
    </ul>
  </div>
</div>

<div class="pull">Nashville isn't where you go to be a big fish. It's where the pond is full of sharks — and the bands that work here every night learn to swim.</div>

<h2>What people say</h2>
<div class="quote">"The band kept the party going all night. When we had a technical problem, they came up with a solution on the spot... they really anticipated every need."<small>— Amber B., San Fernando Valley, CA · Google review</small></div>
<div class="quote">"During the ceremony and reception the band killed it. They kept everything on track... Everyone was cracking up and loved it — it even got the more shy guests out on the floor."<small>— Casey B., Bakersfield, CA · Google review</small></div>
<div class="quote">"Everything ran smooth and the band was the best part of the night... THE BEST!"<small>— Jeannie H., Rosamond, CA · Google review</small></div>

<h2>Repertoire <span class="thin">— {len(songs)} songs, no duplicates</span></h2>
<p class="lede">90s and 2000s country, current country radio, classic and southern rock, and the party songs every room
asks for. Requests are welcome and usually played.</p>
<ul class="setlist">
{rows}
</ul>

<footer>
  <div><strong style="color:var(--paper)">Benny Thomas</strong> · Friends with Benny's<br>
  <a href="tel:+16615330100">(661) 533-0100</a> · <a href="mailto:djbenthomas@gmail.com">djbenthomas@gmail.com</a></div>
  <div style="text-align:right">Private &amp; unlisted — please don't forward publicly.<br>Footage from Lower Broadway, 11/12–11/18/26.</div>
</footer>

</div>
</body>
</html>
'''

open(os.path.join(HERE, 'index.html'), 'w').write(HTML)
print('wrote index.html', len(HTML), 'bytes |', len(songs), 'songs')
