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
    display: inline-block;
    font-size: 0.8em;
    font-weight: 600;
    padding: 0.28em 0.7em;
    border-radius: 999px;
    border: 1px solid var(--svc-accent);
    color: var(--svc-accent);
    background: color-mix(in srgb, var(--svc-accent) 6%, transparent);
    white-space: nowrap;
  }
  a.svc-chip { text-decoration: none; }
  a.svc-chip:hover,
  a.svc-chip:focus {
    color: var(--global-bg-color, #fff);
    background: var(--svc-accent);
    text-decoration: none;
  }
  a.svc-chip:hover .c-yrs,
  a.svc-chip:focus .c-yrs { opacity: 0.85; }
  .svc-chip .c-yrs { opacity: 0.65; font-weight: 500; }

  /* ---- Inline links ---- */
  .svc-list a,
  .svc-lede a,
  .svc-intro a,
  .svc-recog a,
  .svc-geo a {
    color: inherit;
    text-decoration: none;
    border-bottom: 1px solid color-mix(in srgb, var(--svc-accent) 55%, transparent);
  }
  .svc-list a:hover,
  .svc-lede a:hover,
  .svc-intro a:hover,
  .svc-recog a:hover,
  .svc-geo a:hover {
    color: var(--svc-accent);
    border-bottom-color: var(--svc-accent);
  }

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
  <div class="svc-stat"><span class="num">15&times;</span><span class="lbl">Program Chair / Co-Chair appointments (by year)</span></div>
  <div class="svc-stat"><span class="num">15&times;</span><span class="lbl">General Chair appointments (by year)</span></div>
  <div class="svc-stat"><span class="num">215+</span><span class="lbl">Program-committee appointments (each conference-year)</span></div>
  <div class="svc-stat"><span class="num">17</span><span class="lbl">Journal editorial &amp; associate-editor roles held</span></div>
  <div class="svc-stat"><span class="num">45+</span><span class="lbl">Research-funding panels across 15+ agencies &amp; nations</span></div>
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
  <li><span class="role"><a href="https://ics-conference.org/">ACM International Conference on Supercomputing (ICS)</a></span> <span class="yr">— 2024–present</span> (Associate Chair, 2023–2024)</li>
  <li><span class="role"><a href="https://ispass.org/">IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS)</a></span> <span class="yr">— 2022–2023</span></li>
</ul>

<div class="svc-sub">Steering Committee Member</div>
<ul class="svc-list">
  <li><a href="https://ics-conference.org/">ACM International Conference on Supercomputing (ICS)</a> <span class="yr">— 2022–present</span></li>
  <li><a href="https://ispass.org/">IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS)</a> <span class="yr">— 2018–present</span></li>
  <li><a href="https://clustercomp.org/">IEEE International Conference on Cluster Computing (CLUSTER)</a> <span class="yr">— 2009–2011, 2017–2019</span></li>
</ul>

<div class="svc-sub">Program Chair / Co-Chair</div>
<ul class="svc-list">
  <li><span class="role"><a href="https://hpdc.sci.utah.edu/2026/">ACM/IEEE Int&rsquo;l Symposium on High-Performance Parallel and Distributed Computing (HPDC)</a></span> <span class="yr">— 2026</span></li>
  <li><span class="role"><a href="https://ics-conference.org/">ACM International Conference on Supercomputing (ICS)</a></span> <span class="yr">— 2022, 2023</span></li>
  <li><span class="role"><a href="http://datasys.cs.iit.edu/events/CCGrid2014/">IEEE/ACM International Symposium on Cluster, Cloud and Grid Computing (CCGRID)</a></span> <span class="yr">— 2014</span></li>
  <li><a href="https://eurompi.org/">EuroMPI Conference</a> <span class="yr">— 2011</span>; IEEE ScalCom <span class="yr">— 2011</span>; and multiple international workshops (DUAC, 2021&ndash;2025; PASA; PPAC)</li>
</ul>

<div class="svc-sub">Program Vice-Chair / Area Chair</div>
<ul class="svc-list">
  <li><a href="https://www.ipdps.org/">IEEE International Parallel and Distributed Processing Symposium (IPDPS)</a> — Area Chair, Programming Models &amp; Runtime Systems <span class="yr">— 2026</span></li>
  <li><a href="https://www.euro-par.org/">Euro-Par</a> — Global Area Chair, Scheduling and Load Management <span class="yr">— 2022</span></li>
  <li><a href="https://supercomputing.org/">IEEE/ACM Supercomputing (SC)</a> — Area Chair <span class="yr">— 2014</span>; <a href="https://www.ipdps.org/">IPDPS</a> <span class="yr">— 2011</span>; <a href="https://icpp2026.github.io/">ICPP</a> <span class="yr">— 2007</span>; <a href="https://samos-conference.com/">SAMOS</a> <span class="yr">— 2016</span>; <a href="https://www.euro-par.org/">Euro-Par</a> <span class="yr">— 2012</span></li>
</ul>

<div class="svc-sub">General Chair</div>
<ul class="svc-list">
  <li><a href="https://clustercomp.org/">IEEE International Conference on Cluster Computing (CLUSTER)</a> <span class="yr">— 2010, 2018</span></li>
  <li><a href="https://ispass.org/">IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS)</a> <span class="yr">— 2018</span></li>
  <li>Plus eight international workshops at SC, ISC, HiPEAC, ParCo, and ICPP on energy-efficient, approximate, and edge computing <span class="yr">— 2013–2018</span></li>
</ul>

<!-- ============ PROGRAM COMMITTEES ============ -->
<h2 id="program-committees" class="svc-section">Program Committees</h2>
<hr class="svc-rule">
<p class="svc-lede">More than 215 program-committee appointments since 2001 — counting each conference-year separately — across 50+ distinct venues spanning architecture, systems, HPC, and AI, including senior- and area-committee roles.</p>
<div class="svc-chips">
  <a class="svc-chip" href="https://supercomputing.org/">SC <span class="c-yrs">&times;8</span></a>
  <a class="svc-chip" href="https://iscaconf.org/">ISCA</a>
  <a class="svc-chip" href="https://asplos-conference.org/">ASPLOS <span class="c-yrs">&times;2</span></a>
  <a class="svc-chip" href="https://microarch.org/">MICRO <span class="c-yrs">ERC</span></a>
  <a class="svc-chip" href="https://hpca-conf.org/">HPCA</a>
  <a class="svc-chip" href="https://www.aclweb.org/portal/acl">ACL <span class="c-yrs">ERC</span></a>
  <a class="svc-chip" href="https://acmsocc.org/">SoCC <span class="c-yrs">ERC</span></a>
  <a class="svc-chip" href="https://conf.researchr.org/series/PPoPP">PPoPP <span class="c-yrs">&times;6</span></a>
  <a class="svc-chip" href="https://pact2026.github.io/">PACT</a>
  <a class="svc-chip" href="https://aaai.org/conference/aaai/">AAAI <span class="c-yrs">Senior PC</span></a>
  <a class="svc-chip" href="https://www.ipdps.org/">IPDPS <span class="c-yrs">&times;9</span></a>
  <a class="svc-chip" href="https://hpdc.sci.utah.edu/2026/">HPDC</a>
  <a class="svc-chip" href="https://ics-conference.org/">ICS <span class="c-yrs">&times;9</span></a>
  <a class="svc-chip" href="https://icpp2026.github.io/">ICPP <span class="c-yrs">&times;12</span></a>
  <a class="svc-chip" href="https://ccgrid2026.org/">CCGRID</a>
  <a class="svc-chip" href="https://www.euro-par.org/">Euro-Par</a>
  <a class="svc-chip" href="https://clustercomp.org/">CLUSTER</a>
  <a class="svc-chip" href="https://www.isc-hpc.com/">ISC</a>
  <a class="svc-chip" href="https://hipc.org/">HiPC</a>
  <a class="svc-chip" href="https://bigdataieee.org/BigData2026/">IEEE BigData</a>
  <span class="svc-chip">ParCo</span>
  <a class="svc-chip" href="https://www.hipeac.net/">HiPEAC</a>
  <a class="svc-chip" href="https://www.computingfrontiers.org/">Computing Frontiers</a>
  <a class="svc-chip" href="https://www2.sbc.org.br/ce-acpad/sbac-pad/">SBAC-PAD</a>
  <span class="svc-chip">+ 30 more</span>
</div>
<p class="svc-lede" style="margin-top:0.6rem;">Additional committee service includes External Review Committees (<a href="https://microarch.org/">MICRO</a>, <a href="https://conf.researchr.org/series/PPoPP">PPoPP</a>), Reproducibility &amp; Artifact Evaluation (<a href="https://supercomputing.org/">SC</a>, <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=71">IEEE TPDS</a>), the <a href="https://sc17.supercomputing.org/submitters/hpc-impact-showcase/index.html">SC HPC Impact Showcase</a> (Chair, 2017), Tutorials/Workshops chairing at ICS, ISC, and HiPEAC, and Finance Chair at ICS (2009) and EuroMPI (2011). Session Chair on 26 occasions, including the ICS keynote sessions (2022, 2023).</p>

<!-- ============ EDITORIAL ============ -->
<h2 id="editorial" class="svc-section">Editorial Boards &amp; Journals</h2>
<hr class="svc-rule">
<p class="svc-lede">Seventeen editorial appointments across the leading journals in high-performance and sustainable computing. I concluded my four remaining board appointments in 2026.</p>
<ul class="svc-list">
  <li><span class="role"><a href="https://www.sciencedirect.com/journal/computer-physics-communications">Computer Physics Communications</a></span> — HPC Specialist Editor <span class="yr">— 2017–2026</span></li>
  <li><span class="role"><a href="https://journals.sagepub.com/home/hpc">Int&rsquo;l Journal of High Performance Computing Applications (IJHPCA)</a></span> — Associate Editor <span class="yr">— 2012–2026</span></li>
  <li><span class="role"><a href="https://www.sciencedirect.com/journal/journal-of-computational-science">Journal of Computational Science</a></span> — Editorial Board <span class="yr">— 2014–2026</span></li>
  <li><span class="role"><a href="https://www.sciencedirect.com/journal/sustainable-computing-informatics-and-systems">Sustainable Computing: Informatics and Systems (SUSCOM)</a></span> — Editorial Board <span class="yr">— 2010–2026</span> (Guest Editor, 2014)</li>
  <li><span class="role"><a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=71">IEEE Transactions on Parallel and Distributed Systems (TPDS)</a></span> — Associate Editor <span class="yr">— 2018–2021</span>; Best Paper Committee, 2021; Artifact Evaluation Committee, 2020–2021</li>
  <li><a href="https://www.tandfonline.com/journals/gpaa20">Int&rsquo;l Journal of Parallel, Emergent and Distributed Systems (IJPEDS)</a> — Associate Editor <span class="yr">— 2010–2019</span></li>
  <li><a href="https://www.mdpi.com/journal/futureinternet">Future Internet</a> — Editorial Board <span class="yr">— 2020–2026</span>; <a href="https://www.frontiersin.org/journals/high-performance-computing">Frontiers in High Performance Computing</a> — Editor <span class="yr">— 2023–2024</span></li>
  <li>Guest Editor: <a href="https://www.sciencedirect.com/journal/parallel-computing">Parallel Computing</a> (PARCO, 2015), <a href="https://ietresearch.onlinelibrary.wiley.com/journal/ietcdt">IET Computers &amp; Digital Techniques</a> (2014); Editorial Boards: Scientific Programming, <a href="https://onlinelibrary.wiley.com/journal/15320634">CCPE</a>, and earlier venues</li>
</ul>
<p class="svc-lede" style="margin-top:0.6rem;">Sustained reviewing for the field&rsquo;s top journals and publishers — including <a href="https://dl.acm.org/journal/tocs">ACM TOCS</a>, <a href="https://dl.acm.org/journal/toplas">ACM TOPLAS</a>, <a href="https://dl.acm.org/journal/taco">ACM TACO</a>, <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=12">IEEE Transactions on Computers</a>, <a href="https://www.vldb.org/pvldb/">Proceedings of the VLDB Endowment</a>, and <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=40">IEEE Micro</a> — across more than 40 distinct outlets.</p>

<!-- ============ FUNDING PANELS ============ -->
<h2 id="funding" class="svc-section">Research Funding Panels — National &amp; International</h2>
<hr class="svc-rule">
<p class="svc-lede">More than 45 panel and proposal-evaluation appointments — counting each year separately — for government and national funding agencies worldwide.</p>
<div class="svc-cols">
  <div>
    <div class="svc-inst-name">United States</div>
    <ul class="svc-list">
      <li><a href="https://www.nsf.gov">National Science Foundation (NSF)</a> — Panelist <span class="yr">— 2002, 2003, 2004, 2008, 2021, 2023, 2024, 2025</span></li>
      <li><a href="https://science.osti.gov">U.S. Department of Energy (DOE)</a> — Reviewer <span class="yr">— 2020</span></li>
      <li><a href="https://covacci.org/">Coastal Virginia Center for Cyber Innovation (COVA CCI)</a> <span class="yr">— 2021</span>; <a href="https://www.mips.umd.edu/">Maryland Industrial Partnerships</a> <span class="yr">— 2007</span>; <a href="https://www.bsf.org.il">U.S.–Israel Binational Science Foundation</a> <span class="yr">— 2009</span></li>
    </ul>
  </div>
  <div>
    <div class="svc-inst-name">United Kingdom &amp; European Union</div>
    <ul class="svc-list">
      <li><a href="https://www.ukri.org/councils/epsrc/">UK EPSRC</a> — Reviewer &amp; Platform Grant Panelist <span class="yr">— 2012–2021</span></li>
      <li><a href="https://raeng.org.uk">Royal Academy of Engineering (UK)</a> <span class="yr">— 2015, 2017</span></li>
      <li><a href="https://erc.europa.eu">European Research Council (ERC)</a> <span class="yr">— 2020</span>; <a href="https://cordis.europa.eu/programme/id/FP7">European Commission FP7</a> <span class="yr">— 2012–2016</span></li>
    </ul>
  </div>
  <div>
    <div class="svc-inst-name">Europe (national agencies)</div>
    <ul class="svc-list">
      <li><a href="https://anr.fr/en/">French National Research Agency (ANR)</a> — Panelist <span class="yr">— 2025</span></li>
      <li><a href="https://www.snf.ch/en">Swiss National Science Foundation</a> <span class="yr">— 2016, 2020, 2025</span></li>
      <li><a href="https://www.elidek.gr/en/homepage/">Hellenic Foundation for Research &amp; Innovation (Greece)</a> <span class="yr">— 2024, 2025</span></li>
      <li><a href="https://www.oeaw.ac.at/en/">Austrian Academy of Sciences</a> <span class="yr">— 2017</span>; Italy (<a href="https://www.cineca.it/en">CINECA</a>) <span class="yr">— 2021</span>; Sweden (<a href="https://www.kks.se/en/">KK-Stiftelsen</a>) <span class="yr">— 2021</span>; Netherlands (<a href="https://www.nwo.nl/en">STW, now NWO</a>) <span class="yr">— 2016</span>; Poland (<a href="https://www.ncn.gov.pl/en">NSC</a>) <span class="yr">— 2016</span>; Cyprus (<a href="https://www.research.org.cy/en/">RIF</a>) <span class="yr">— 2016</span></li>
    </ul>
  </div>
  <div>
    <div class="svc-inst-name">Canada</div>
    <ul class="svc-list">
      <li><a href="https://nserc-crsng.canada.ca/en">NSERC</a> — Discovery Grants Panelist <span class="yr">— 2014, 2015, 2016</span> (Reviewer, 2007)</li>
    </ul>
  </div>
</div>

<!-- ============ EXTERNAL LEADERSHIP ============ -->
<h2 id="external" class="svc-section">External Leadership, Advisory &amp; Evaluation</h2>
<hr class="svc-rule">
<ul class="svc-list">
  <li><span class="role"><a href="https://cra.org">Computing Research Association (CRA)</a></span> — <a href="https://cra.org/cra-leadership-academy/">Leadership Academy</a> Committee <span class="yr">— 2024–present</span></li>
  <li><a href="https://www.aaas.org/">American Association for the Advancement of Science (AAAS)</a> — Session Reviewer <span class="yr">— 2024</span></li>
  <li>Scientific Advisory Board, <a href="https://www.ni-hpc.ac.uk/Kelvin2/">Kelvin Tier-2 HPC Centre</a>, Queen&rsquo;s University Belfast <span class="yr">— 2021–present</span></li>
  <li>Faculty Appointment Committees: <a href="https://www.ntnu.edu/">NTNU, Norway</a> <span class="yr">— 2022</span>; <a href="https://www.uni-heidelberg.de/en">Heidelberg University, Germany</a> <span class="yr">— 2021</span>; <a href="https://uoi.gr/en/">University of Ioannina, Greece</a> <span class="yr">— 2022</span></li>
  <li>External Accreditation &amp; Evaluation Panels: <a href="https://www.eap.gr/en/">Hellenic Open University</a> <span class="yr">— 2023</span>; <a href="https://uoi.gr/en/">University of Ioannina</a> <span class="yr">— 2022</span>; <a href="https://www.demokritos.gr/en/">NCSR Demokritos, Greece</a> <span class="yr">— 2022</span>; FORTH-ICS Seed Grants <span class="yr">— 2021–present</span></li>
  <li>Scientific Advisory Board, <a href="https://marie-sklodowska-curie-actions.ec.europa.eu/">Marie Curie Individual Fellowship</a> <span class="yr">— 2022</span></li>
  <li>Scientific Advisory Board, <a href="https://www.ics.forth.gr/">Institute of Computer Science, FORTH, Greece</a> <span class="yr">— 2020–present</span>; Evaluation Panel, FORTH Synergy Grants <span class="yr">— 2019–present</span></li>
  <li><a href="https://www.ukri.org/councils/epsrc/">UK EPSRC</a> Strategic Advisory Team (SAT) — e-Infrastructure <span class="yr">— 2018–present</span></li>
  <li>External Examiner, <a href="https://eps.leeds.ac.uk/computing">School of Computing, University of Leeds</a> <span class="yr">— 2012–present</span></li>
  <li><a href="https://www.computer.org">IEEE Computer Society</a> — Senior Membership Reviewer <span class="yr">— 2025–2026</span></li>
</ul>

<!-- ============ UNIVERSITY LEADERSHIP ============ -->
<h2 id="university" class="svc-section">University &amp; Departmental Leadership</h2>
<hr class="svc-rule">
<div class="svc-cols">
  <div>
    <div class="svc-inst-name"><a href="https://www.cs.vt.edu/">Virginia Tech</a></div>
    <ul class="svc-list">
      <li><a href="https://eng.vt.edu/">College of Engineering</a> Promotion &amp; Tenure Committee <span class="yr">— 2025–present</span></li>
      <li>Computer Science Personnel Committee — Chair <span class="yr">— 2025–present</span> (Associate Chair, 2024–2025; member since 2022)</li>
      <li>Computer Science Qualifying Exam Committee — Chair, Systems, Networking &amp; Cybersecurity <span class="yr">— 2026</span></li>
      <li>Associate Director, <a href="https://cs.vt.edu/research/research-areas/systems.html">Stacks@CS Center for Computer Systems Research</a> <span class="yr">— 2022–present</span></li>
      <li>Department Head Search Committee <span class="yr">— 2023–2024</span>; <a href="https://www.research.vt.edu/research-development/professional-development/proposal-development-institute.html">University Proposal Development Institute</a> Mentor <span class="yr">— 2024–present</span></li>
    </ul>
  </div>
  <div>
    <div class="svc-inst-name"><a href="https://www.qub.ac.uk">Queen&rsquo;s University Belfast</a></div>
    <ul class="svc-list">
      <li>Head of School, <a href="https://www.qub.ac.uk/schools/eeecs/">Electronics, Electrical Engineering &amp; Computer Science</a> <span class="yr">— 2016–2018</span></li>
      <li>Director, ECIT Global Innovation Institute <span class="yr">— 2018–2019</span>; Acting Director, Centre for Data Science &amp; Scalable Computing <span class="yr">— 2016–2019</span></li>
      <li>REF Champion (Computer Science &amp; Engineering); Faculty Executive Board <span class="yr">— 2016–2019</span>; Academic Council <span class="yr">— 2016–2018</span></li>
      <li>Chair, University HPC Advisory Group <span class="yr">— 2012–2019</span>; Vice-Chancellor Selection Panel <span class="yr">— 2017</span></li>
    </ul>
  </div>
</div>
<p class="svc-lede" style="margin-top:0.9rem;">As Head of School at Queen&rsquo;s, the School of EEECS earned the <a href="https://www.advance-he.ac.uk/equality-charters/athena-swan-charter">Athena SWAN Silver</a> and <a href="https://www.investorsinpeople.com/">Investors in People Silver</a> awards for diversity and inclusion, and reached record research expenditure and enrollment.</p>

<!-- ============ SOCIETIES ============ -->
<h2 id="societies" class="svc-section">Professional Societies &amp; Fellowships</h2>
<hr class="svc-rule">
<ul class="svc-list">
  <li><span class="role"><a href="https://www.ieee.org">IEEE</a></span> — <a href="https://www.ieee.org/membership/fellows/index.html">Fellow</a> (2024), <a href="https://www.computer.org/communities/professional-chapters/distinguished-visitors-program">Distinguished Visitor</a> (2024–present), Distinguished Contributor (2022–present)</li>
  <li><span class="role"><a href="https://www.acm.org">ACM</a></span> — <a href="https://awards.acm.org/distinguished-members">Distinguished Member</a> (2018–present); member of <a href="https://www.sigarch.org">SIGARCH</a>, <a href="https://www.sigops.org">SIGOPS</a>, and <a href="https://www.sighpc.org">SIGHPC</a></li>
  <li>Fellow — <a href="https://www.aaia-ai.org/">Asia-Pacific AI Association (AAIA)</a>, International AI Industry Alliance (AIIA), <a href="https://www.bcs.org">British Computer Society (BCS)</a>, and the <a href="https://www.theiet.org">Institution of Engineering &amp; Technology (IET)</a></li>
  <li>Full Member, <a href="https://www.sigmaxi.org">Sigma Xi</a>; Chartered Engineer (CEng); Member, <a href="https://web.tee.gr/">Technical Chamber of Greece</a>; former member, <a href="https://cphc.ac.uk/">UK Council of Professors &amp; Heads of Computing (CPHC)</a></li>
</ul>

<!-- ============ RECOGNITION ============ -->
<h2 id="recognition" class="svc-section">Recognition for Service</h2>
<hr class="svc-rule">
<div class="svc-recog">
  <ul>
    <li><strong>Outstanding Service Award</strong>, <a href="https://cs.vt.edu/">Department of Computer Science</a>, Virginia Tech (2026)</li>
    <li><strong>IEEE Award for Editorial Excellence</strong>, <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=71">IEEE Transactions on Parallel and Distributed Systems</a> (2020)</li>
    <li><strong>Elsevier Distinguished Editorial Service Award</strong> (2019)</li>
    <li><strong>IEEE Outstanding Service Awards</strong> (2010, 2014, 2018)</li>
    <li>Editorial Excellence recognition from <a href="https://www.sciencedirect.com/journal/sustainable-computing-informatics-and-systems"><em>Sustainable Computing: Informatics and Systems</em></a></li>
  </ul>
</div>

<!-- ============ PUBLIC ENGAGEMENT ============ -->
<h2 id="public" class="svc-section">Public Engagement &amp; Outreach</h2>
<hr class="svc-rule">
<p class="svc-lede">Translating computing research for broad audiences — on AI, supercomputing, and the societal and economic impact of data centers.</p>
<ul class="svc-list">
  <li><span class="role"><a href="https://tedxmidatlantic.com/">TEDxMidAtlantic</a></span> — &ldquo;Myths and Ways Forward for AI&rdquo; <span class="yr">— Nov 2025</span></li>
  <li><span class="role">More to Know Podcast</span> — &ldquo;<a href="https://open.spotify.com/episode/4n6PU32xwqamUgKYGkBlDf">The Future of Data Centers: AI, Energy Demand, and the Next Tech Infrastructure Boom</a>&rdquo; <span class="yr">— Feb 2026</span></li>
  <li><span class="role">FuelCell Energy</span> — &ldquo;<a href="https://www.fuelcellenergy.com/blog/caught-in-the-current-how-data-centers-are-trading-carbon-goals-for-capacity">On the societal and economic implications of data centers</a>&rdquo; <span class="yr">— Dec 2025</span></li>
  <li>Press &amp; media on the societal and economic implications of data centers — Cardinal News, Roanoke Times, MSN/WFXR, Northwest Indiana Times, and others <span class="yr">— 2024–2025</span></li>
  <li>Invited conference panelist — <a href="https://supercomputing.org/">SC</a> (2020), EPSRC Manycore Computing (2018), <a href="https://icpp2026.github.io/">ICPP</a> (2010), IBM ExaChallenge (2012), and Microsoft Faculty Research Summit</li>
</ul>
