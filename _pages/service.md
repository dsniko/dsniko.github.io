---
layout: archive
title: "Service"
permalink: /service/
author_profile: true
---

<style>
  /* ===== Service page ===== */
  :root {
    --svc-accent: var(--global-link-color, #52adc8);
  }

  .svc-intro {
    font-size: 1.0em;
    line-height: 1.6;
    opacity: 0.92;
    margin: 0 0 1.75rem;
  }

  /* ---- Stat tiles ---- */
  .svc-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 0.75rem;
    margin: 0 0 2rem;
  }
  .svc-stat {
    border: 1px solid var(--global-border-color, #e6e6e6);
    border-top: 3px solid var(--svc-accent);
    border-radius: 8px;
    padding: 0.9rem 0.9rem 0.8rem;
    background: color-mix(in srgb, var(--svc-accent) 5%, transparent);
  }
  .svc-stat .num {
    display: block;
    font-size: 1.7em;
    font-weight: 800;
    line-height: 1.05;
    color: var(--svc-accent);
  }
  .svc-stat .lbl {
    display: block;
    font-size: 0.82em;
    opacity: 0.85;
    margin-top: 0.25rem;
  }

  /* ---- Geographic breadth strip ---- */
  .svc-geo {
    border-left: 4px solid var(--svc-accent);
    background: color-mix(in srgb, var(--svc-accent) 7%, transparent);
    padding: 0.85rem 1.1rem;
    border-radius: 0 6px 6px 0;
    margin: 0 0 2.5rem;
  }
  .svc-geo .geo-label {
    display: block;
    font-size: 0.68em;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--svc-accent);
    margin-bottom: 0.45rem;
  }
  .svc-geo .geo-list { font-size: 0.92em; line-height: 1.8; }

  /* ---- Section headers ---- */
  .svc-section {
    margin-top: 2.6rem;
    margin-bottom: 0.3rem;
    scroll-margin-top: 90px;
    font-size: 1.35em;
  }
  .svc-section + .svc-rule {
    margin: 0.3rem 0 1.25rem;
    border: 0;
    border-top: 2px solid var(--svc-accent);
    opacity: 0.35;
  }
  .svc-lede { font-size: 0.93em; opacity: 0.85; margin: 0 0 1.1rem; }

  /* ---- Role list ---- */
  .svc-list { margin: 0 0 0.5rem; padding: 0; list-style: none; }
  .svc-list li {
    margin: 0 0 0.7rem;
    padding-left: 1.1rem;
    position: relative;
    font-size: 0.94em;
    line-height: 1.5;
  }
  .svc-list li::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0.55em;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--svc-accent);
  }
  .svc-list .role { font-weight: 700; }
  .svc-list .yr { opacity: 0.7; font-size: 0.92em; white-space: nowrap; }

  /* ---- Sub-group label ---- */
  .svc-sub {
    font-weight: 700;
    font-size: 0.82em;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--svc-accent);
    margin: 1.3rem 0 0.5rem;
  }

  /* ---- Venue chips ---- */
  .svc-chips { display: flex; flex-wrap: wrap; gap: 0.45rem; margin: 0.4rem 0 0.8rem; }
  .svc-chip {
    font-size: 0.8em;
    font-weight: 600;
    padding: 0.28em 0.7em;
    border-radius: 999px;
    border: 1px solid var(--svc-accent);
    color: var(--svc-accent);
    background: color-mix(in srgb, var(--svc-accent) 6%, transparent);
    white-space: nowrap;
  }
  .svc-chip .c-yrs { opacity: 0.65; font-weight: 500; }

  /* ---- Two-column institution blocks ---- */
  .svc-cols {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.25rem 1.75rem;
  }
  .svc-inst-name {
    font-weight: 700;
    font-size: 0.98em;
    margin: 0 0 0.5rem;
    padding-bottom: 0.3rem;
    border-bottom: 1px solid var(--global-border-color, #e6e6e6);
  }

  /* ---- Recognition callout ---- */
  .svc-recog {
    border: 1px solid var(--global-border-color, #e6e6e6);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin: 0.4rem 0 0;
    background: var(--global-footer-bg-color, #f7f8f8);
  }
  .svc-recog ul { margin: 0; padding-left: 1.1rem; }
  .svc-recog li { margin: 0 0 0.45rem; font-size: 0.92em; }
</style>

<p class="svc-intro">
Across more than two decades, my service to the computing community has spanned the leadership of
flagship conferences and journals, hundreds of peer-review and program-committee appointments, and
research-funding evaluation for national agencies on four continents — alongside sustained academic
leadership at Virginia Tech and Queen&rsquo;s University Belfast. The record below captures both the
breadth and the depth of that engagement, nationally and internationally.
</p>

<!-- ============ STATS ============ -->
<div class="svc-stats">
  <div class="svc-stat"><span class="num">2</span><span class="lbl">Flagship conferences led as Steering Committee Chair (ICS, ISPASS)</span></div>
  <div class="svc-stat"><span class="num">9&times;</span><span class="lbl">Program Chair / Co-Chair appointments</span></div>
  <div class="svc-stat"><span class="num">10&times;</span><span class="lbl">General Chair appointments</span></div>
  <div class="svc-stat"><span class="num">55+</span><span class="lbl">Program-committee appointments</span></div>
  <div class="svc-stat"><span class="num">17</span><span class="lbl">Journal editorial &amp; associate-editor roles</span></div>
  <div class="svc-stat"><span class="num">40+</span><span class="lbl">Research-funding panels across 15+ agencies &amp; nations</span></div>
</div>

<!-- ============ GEOGRAPHIC BREADTH ============ -->
<div class="svc-geo">
  <span class="geo-label">Funding &amp; evaluation service spanning</span>
  <div class="geo-list">
    United States &middot; United Kingdom &middot; European Union &middot; Canada &middot; France &middot;
    Switzerland &middot; Germany &middot; Italy &middot; Netherlands &middot; Austria &middot; Sweden &middot;
    Poland &middot; Norway &middot; Greece &middot; Cyprus &middot; Israel (binational)
  </div>
</div>

<!-- ============ CONFERENCE LEADERSHIP ============ -->
<h2 id="leadership" class="svc-section">Conference &amp; Community Leadership</h2>
<hr class="svc-rule">
<p class="svc-lede">Steering, chairing, and shaping the direction of the field&rsquo;s leading systems and high-performance computing venues.</p>

<div class="svc-sub">Steering Committee Chair</div>
<ul class="svc-list">
  <li><span class="role">ACM International Conference on Supercomputing (ICS)</span> <span class="yr">— 2024–present</span> (Associate Chair, 2023–2024)</li>
  <li><span class="role">IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS)</span> <span class="yr">— 2022–2023</span></li>
</ul>

<div class="svc-sub">Steering Committee Member</div>
<ul class="svc-list">
  <li>ACM International Conference on Supercomputing (ICS) <span class="yr">— 2022–present</span></li>
  <li>IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS) <span class="yr">— 2018–present</span></li>
  <li>IEEE International Conference on Cluster Computing (CLUSTER) <span class="yr">— 2009–2011, 2017–2019</span></li>
</ul>

<div class="svc-sub">Program Chair / Co-Chair</div>
<ul class="svc-list">
  <li><span class="role">ACM/IEEE Int&rsquo;l Symposium on High-Performance Parallel and Distributed Computing (HPDC)</span> <span class="yr">— 2026</span></li>
  <li><span class="role">ACM International Conference on Supercomputing (ICS)</span> <span class="yr">— 2022, 2023</span></li>
  <li><span class="role">IEEE/ACM International Symposium on Cluster, Cloud and Grid Computing (CCGRID)</span> <span class="yr">— 2014</span></li>
  <li>EuroMPI Conference <span class="yr">— 2011</span>; IEEE ScalCom <span class="yr">— 2011</span>; and multiple international workshops (DUAC, PASA, PPAC)</li>
</ul>

<div class="svc-sub">Program Vice-Chair / Area Chair</div>
<ul class="svc-list">
  <li>IEEE International Parallel and Distributed Processing Symposium (IPDPS) — Area Chair, Programming Models &amp; Runtime Systems <span class="yr">— 2026</span></li>
  <li>EuroPar — Global Area Chair, Scheduling and Load Management <span class="yr">— 2022</span></li>
  <li>IEEE/ACM Supercomputing (SC) — Area Chair <span class="yr">— 2014</span>; IPDPS <span class="yr">— 2011</span>; ICPP <span class="yr">— 2007</span>; SAMOS <span class="yr">— 2016</span>; EuroPar <span class="yr">— 2012</span></li>
</ul>

<div class="svc-sub">General Chair</div>
<ul class="svc-list">
  <li>IEEE International Conference on Cluster Computing (CLUSTER) <span class="yr">— 2010, 2018</span></li>
  <li>IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS) <span class="yr">— 2018</span></li>
  <li>Plus seven international workshops at SC, ISC, HiPEAC, ParCo, and ICPP on energy-efficient, approximate, and edge computing <span class="yr">— 2013–2018</span></li>
</ul>

<!-- ============ PROGRAM COMMITTEES ============ -->
<h2 id="program-committees" class="svc-section">Program Committees</h2>
<hr class="svc-rule">
<p class="svc-lede">More than 55 program-committee appointments since 2001 across 30+ distinct venues — spanning architecture, systems, HPC, and AI — including senior- and area-committee roles.</p>
<div class="svc-chips">
  <span class="svc-chip">SC <span class="c-yrs">&times;6</span></span>
  <span class="svc-chip">ISCA</span>
  <span class="svc-chip">ASPLOS <span class="c-yrs">&times;2</span></span>
  <span class="svc-chip">MICRO <span class="c-yrs">ERC</span></span>
  <span class="svc-chip">HPCA</span>
  <span class="svc-chip">PPoPP <span class="c-yrs">&times;6</span></span>
  <span class="svc-chip">PACT</span>
  <span class="svc-chip">AAAI <span class="c-yrs">Senior PC</span></span>
  <span class="svc-chip">IPDPS <span class="c-yrs">&times;9</span></span>
  <span class="svc-chip">HPDC</span>
  <span class="svc-chip">ICS <span class="c-yrs">&times;9</span></span>
  <span class="svc-chip">ICPP <span class="c-yrs">&times;12</span></span>
  <span class="svc-chip">CCGRID</span>
  <span class="svc-chip">EuroPar</span>
  <span class="svc-chip">CLUSTER</span>
  <span class="svc-chip">ISC</span>
  <span class="svc-chip">HiPC</span>
  <span class="svc-chip">IEEE BigData</span>
  <span class="svc-chip">ParCo</span>
  <span class="svc-chip">HiPEAC</span>
  <span class="svc-chip">Computing Frontiers</span>
  <span class="svc-chip">SBAC-PAD</span>
  <span class="svc-chip">+ 30 more</span>
</div>
<p class="svc-lede" style="margin-top:0.6rem;">Additional committee service includes External Review Committees (MICRO, PPoPP), Reproducibility &amp; Artifact Evaluation (SC, IEEE TPDS), the SC HPC Impact Showcase (Chair, 2017), and Tutorials/Workshops chairing at ICS, ISC, HiPEAC, and EuroMPI. Session Chair on 20 occasions, including the ICS keynote sessions (2022, 2023).</p>

<!-- ============ EDITORIAL ============ -->
<h2 id="editorial" class="svc-section">Editorial Boards &amp; Journals</h2>
<hr class="svc-rule">
<p class="svc-lede">Seventeen editorial appointments across the leading journals in high-performance and sustainable computing.</p>
<ul class="svc-list">
  <li><span class="role">Computer Physics Communications</span> — HPC Specialist Editor <span class="yr">— 2017–present</span></li>
  <li><span class="role">Int&rsquo;l Journal of High Performance Computing Applications (IJHPCA)</span> — Associate Editor <span class="yr">— 2012–present</span></li>
  <li><span class="role">Journal of Computational Science</span> — Editorial Board <span class="yr">— 2014–present</span></li>
  <li><span class="role">Sustainable Computing: Informatics and Systems (SUSCOM)</span> — Editorial Board <span class="yr">— 2010–present</span> (Guest Editor, 2014)</li>
  <li><span class="role">IEEE Transactions on Parallel and Distributed Systems (TPDS)</span> — Associate Editor <span class="yr">— 2018–2021</span>; Best Paper &amp; Artifact Evaluation Committees, 2020–2021</li>
  <li>Int&rsquo;l Journal of Parallel, Emergent and Distributed Systems (IJPEDS) — Associate Editor <span class="yr">— 2010–2019</span></li>
  <li>Future Internet — Editorial Board <span class="yr">— 2020–2026</span>; Frontiers in High-Performance Computing — Editor <span class="yr">— 2023–2024</span></li>
  <li>Guest Editor: Parallel Computing (PARCO, 2015), IET Computers &amp; Digital Techniques (2014); Editorial Boards: Scientific Programming, CCPE, and earlier venues</li>
</ul>
<p class="svc-lede" style="margin-top:0.6rem;">Sustained reviewing for the field&rsquo;s top journals and publishers — including ACM TOCS, ACM TOPLAS, ACM TACO, IEEE Transactions on Computers, Proceedings of the VLDB Endowment, and IEEE Micro — across more than 40 distinct outlets.</p>

<!-- ============ FUNDING PANELS ============ -->
<h2 id="funding" class="svc-section">Research Funding Panels — National &amp; International</h2>
<hr class="svc-rule">
<p class="svc-lede">More than 40 panel and proposal-evaluation appointments for government and national funding agencies worldwide.</p>
<div class="svc-cols">
  <div>
    <div class="svc-inst-name">United States</div>
    <ul class="svc-list">
      <li>National Science Foundation (NSF) — Panelist <span class="yr">— 2002, 2003, 2004, 2008, 2021, 2023, 2024, 2025</span></li>
      <li>U.S. Department of Energy (DOE) — Reviewer <span class="yr">— 2020</span></li>
      <li>Coastal Virginia Center for Cyber Innovation (COVA CCI) <span class="yr">— 2021</span>; Maryland Industrial Partnerships <span class="yr">— 2007</span>; U.S.–Israel Binational Science Foundation <span class="yr">— 2009</span></li>
    </ul>
  </div>
  <div>
    <div class="svc-inst-name">United Kingdom &amp; European Union</div>
    <ul class="svc-list">
      <li>UK EPSRC — Reviewer &amp; Platform Grant Panelist <span class="yr">— 2012–2021</span></li>
      <li>Royal Academy of Engineering (UK) <span class="yr">— 2015, 2017</span></li>
      <li>European Research Council (ERC) <span class="yr">— 2020</span>; European Commission FP7 <span class="yr">— 2012–2016</span></li>
    </ul>
  </div>
  <div>
    <div class="svc-inst-name">Europe (national agencies)</div>
    <ul class="svc-list">
      <li>French National Research Agency (ANR) — Panelist <span class="yr">— 2025</span></li>
      <li>Swiss National Science Foundation <span class="yr">— 2016, 2020, 2025</span></li>
      <li>Hellenic Foundation for Research &amp; Innovation (Greece) <span class="yr">— 2024, 2025</span></li>
      <li>Austrian Academy of Sciences <span class="yr">— 2017</span>; Italy (CINECA) <span class="yr">— 2021</span>; Sweden (KK-Stiftelsen) <span class="yr">— 2021</span>; Netherlands (STW) <span class="yr">— 2016</span>; Poland (NSC) <span class="yr">— 2016</span>; Cyprus <span class="yr">— 2016</span></li>
    </ul>
  </div>
  <div>
    <div class="svc-inst-name">Canada</div>
    <ul class="svc-list">
      <li>NSERC — Discovery Grants Panelist <span class="yr">— 2014, 2015, 2016</span> (Reviewer, 2007)</li>
    </ul>
  </div>
</div>

<!-- ============ EXTERNAL LEADERSHIP ============ -->
<h2 id="external" class="svc-section">External Leadership, Advisory &amp; Evaluation</h2>
<hr class="svc-rule">
<ul class="svc-list">
  <li><span class="role">Computing Research Association (CRA)</span> — Leadership Academy Committee <span class="yr">— 2024–present</span></li>
  <li>American Association for the Advancement of Science (AAAS) — Session Reviewer <span class="yr">— 2024</span></li>
  <li>Scientific Advisory Board, Kelvin Tier-2 HPC Centre, Queen&rsquo;s University Belfast <span class="yr">— 2021–present</span></li>
  <li>Faculty Appointment Committees: NTNU, Norway <span class="yr">— 2022</span>; Heidelberg University, Germany <span class="yr">— 2021</span>; University of Ioannina, Greece <span class="yr">— 2022</span></li>
  <li>External Accreditation &amp; Evaluation Panels: Hellenic Open University <span class="yr">— 2023</span>; University of Ioannina <span class="yr">— 2022</span>; NCSR Demokritos, Greece <span class="yr">— 2022</span>; FORTH-ICS Seed Grants <span class="yr">— 2021–present</span></li>
  <li>Scientific Advisory Board, Marie Curie Individual Fellowship <span class="yr">— 2022</span></li>
</ul>

<!-- ============ UNIVERSITY LEADERSHIP ============ -->
<h2 id="university" class="svc-section">University &amp; Departmental Leadership</h2>
<hr class="svc-rule">
<div class="svc-cols">
  <div>
    <div class="svc-inst-name">Virginia Tech</div>
    <ul class="svc-list">
      <li>College of Engineering Promotion &amp; Tenure Committee <span class="yr">— 2025–present</span></li>
      <li>Computer Science Personnel Committee — Chair <span class="yr">— 2025–present</span> (member since 2022)</li>
      <li>Associate Director, Stacks@CS Center for Computer Systems Research <span class="yr">— 2022–present</span></li>
      <li>Department Head Search Committee <span class="yr">— 2023–2024</span>; University Proposal Development Institute Mentor <span class="yr">— 2024–present</span></li>
    </ul>
  </div>
  <div>
    <div class="svc-inst-name">Queen&rsquo;s University Belfast</div>
    <ul class="svc-list">
      <li>Head of School, Electronics, Electrical Engineering &amp; Computer Science <span class="yr">— 2016–2018</span></li>
      <li>Director, ECIT Global Innovation Institute <span class="yr">— 2018–2019</span>; Director, Centre for Data Science &amp; Scalable Computing</li>
      <li>REF Champion (Computer Science &amp; Engineering); Faculty Executive Board; Academic Council <span class="yr">— 2016–2019</span></li>
      <li>Chair, University HPC Advisory Group <span class="yr">— 2012–2019</span>; Vice-Chancellor Selection Panel <span class="yr">— 2017</span></li>
    </ul>
  </div>
</div>
<p class="svc-lede" style="margin-top:0.9rem;">As Head of School at Queen&rsquo;s, the School of EEECS earned the Athena SWAN Silver and Investors in People Silver awards for diversity and inclusion, and reached record research expenditure and enrollment.</p>

<!-- ============ SOCIETIES ============ -->
<h2 id="societies" class="svc-section">Professional Societies &amp; Fellowships</h2>
<hr class="svc-rule">
<ul class="svc-list">
  <li><span class="role">IEEE</span> — Fellow (2024), Distinguished Visitor (2024–present), Distinguished Contributor (2022–present)</li>
  <li><span class="role">ACM</span> — Distinguished Member (2018–present); member of SIGARCH, SIGOPS, and SIGHPC</li>
  <li>Fellow — Asia-Pacific AI Association (AAIA), International AI Industry Alliance (AIIA), British Computer Society (BCS), and the Institution of Engineering &amp; Technology (IET)</li>
  <li>Full Member, Sigma Xi; Chartered Engineer (CEng); Member, Technical Chamber of Greece; former member, UK Council of Professors &amp; Heads of Computing (CPHC)</li>
</ul>

<!-- ============ RECOGNITION ============ -->
<h2 id="recognition" class="svc-section">Recognition for Service</h2>
<hr class="svc-rule">
<div class="svc-recog">
  <ul>
    <li><strong>IEEE Award for Editorial Excellence</strong>, IEEE Transactions on Parallel and Distributed Systems (2020)</li>
    <li><strong>Elsevier Distinguished Editorial Service Award</strong> (2019)</li>
    <li><strong>IEEE Outstanding Service Awards</strong> (2010, 2014, 2018)</li>
    <li>Editorial Excellence recognition from <em>Sustainable Computing: Informatics and Systems</em></li>
  </ul>
</div>

<!-- ============ PUBLIC ENGAGEMENT ============ -->
<h2 id="public" class="svc-section">Public Engagement &amp; Outreach</h2>
<hr class="svc-rule">
<p class="svc-lede">Translating computing research for broad audiences — on AI, supercomputing, and the societal and economic impact of data centers.</p>
<ul class="svc-list">
  <li><span class="role">TEDxMidAtlantic</span> — &ldquo;Myths and Ways Forward for AI&rdquo; <span class="yr">— Nov 2025</span></li>
  <li><span class="role">More to Know Podcast</span> — &ldquo;The Future of Data Centers: AI, Energy Demand, and the Next Infrastructure Boom&rdquo; <span class="yr">— Feb 2026</span></li>
  <li>Press &amp; media on the societal and economic implications of data centers — Cardinal News, Roanoke Times, MSN/WFXR, Northwest Indiana Times, and others <span class="yr">— 2024–2025</span></li>
  <li>Invited conference panelist — SC (2020), EPSRC Manycore Computing (2018), ICPP (2010), IBM ExaChallenge (2012), and Microsoft Faculty Research Summit</li>
</ul>
