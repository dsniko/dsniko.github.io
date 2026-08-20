---
layout: archive
title: "Mentees"
permalink: /mentees/
author_profile: true
---

<!--
  Redesigned Mentees page — drop-in replacement for _pages/mentees.md
  Requires the companion styles in _sass/_mentees.scss (import once in assets/css/main.scss).
  All content is still driven by the _mentees collection, so nothing here needs manual upkeep.
-->

{% assign current_students = site.mentees | where: "status", "current" %}
{% assign phd_alumni      = site.mentees | where: "status", "alumni" | where: "category", "phd" %}
{% assign postdoc_alumni  = site.mentees | where: "status", "alumni" | where: "category", "postdoc" %}
{% assign masters_alumni  = site.mentees | where: "status", "alumni" | where: "category", "masters" %}
{% assign undergrad_alumni = site.mentees | where: "status", "alumni" | where: "category", "undergrad" %}
{% assign phd_current_n = current_students | where: "category", "phd" | size %}
{% assign phd_total = phd_alumni.size | plus: phd_current_n %}
{% assign all_alumni = site.mentees | where: "status", "alumni" %}

<p class="mentees-intro">Over more than two decades, I have had the privilege of mentoring
<strong>{{ site.mentees | size }} researchers</strong> — from undergraduates to postdoctoral
scholars — who have gone on to leading roles across industry, academia, and the national laboratories.</p>

<!-- ============ STATS BAND ============ -->
<div class="mentee-stats">
  <div class="mstat mstat--total"><span class="num">{{ site.mentees | size }}</span><span class="lbl">Total mentees</span></div>
  <div class="mstat"><span class="num">{{ phd_total }} <small>({{ phd_current_n }} current)</small></span><span class="lbl">PhD students</span></div>
  <div class="mstat"><span class="num">{{ postdoc_alumni.size }}</span><span class="lbl">Postdocs</span></div>
  <div class="mstat"><span class="num">{{ masters_alumni.size }}</span><span class="lbl">Master&rsquo;s</span></div>
  <div class="mstat"><span class="num">{{ undergrad_alumni.size }}</span><span class="lbl">Undergraduates</span></div>
</div>

<!-- ============ PLACEMENT BAND (auto-computed from current_position) ============ -->
{% assign ind = 0 %}{% assign aca = 0 %}{% assign lab = 0 %}
{% for m in all_alumni %}{% assign p = m.current_position %}{% if p and p != "" %}{% if p contains "Livermore" or p contains "Argonne" or p contains "National Laborator" or p contains "National Institutes" or p contains "Barcelona Supercomputing" or p contains "Imec" or p contains "FORTH" or p contains "Marine Research" %}{% assign lab = lab | plus: 1 %}{% elsif p contains "Professor" or p contains "Lecturer" or p contains "Faculty" or p contains "University" or p contains "Postdoc" or p contains "Collegiate" or p contains "Research Fellow" or p contains "Teaching Assistant" or p contains "Graduate" or p contains "Masters Student" or p contains "Visiting Scholar" %}{% assign aca = aca | plus: 1 %}{% else %}{% assign ind = ind | plus: 1 %}{% endif %}{% endif %}{% endfor %}
{% assign known = ind | plus: aca | plus: lab %}
{% assign indpct = ind | times: 100 | divided_by: known %}{% assign acapct = aca | times: 100 | divided_by: known %}{% assign labpct = lab | times: 100 | divided_by: known %}

<div class="mentee-placement">
  <h2>Where they are now</h2>
  <p class="sub">Known placements of {{ known }} graduated mentees</p>
  <div class="pbar">
    <span style="width:{{ indpct }}%" class="seg-ind"></span>
    <span style="width:{{ acapct }}%" class="seg-aca"></span>
    <span style="width:{{ labpct }}%" class="seg-lab"></span>
  </div>
  <div class="plegend">
    <span><i class="seg-ind"></i><strong>{{ ind }}</strong> in industry</span>
    <span><i class="seg-aca"></i><strong>{{ aca }}</strong> in academia</span>
    <span><i class="seg-lab"></i><strong>{{ lab }}</strong> at national labs &amp; institutes</span>
  </div>
</div>

<!-- ============ CURRENT STUDENTS — CARD GRID ============ -->
<h2 id="current-students" class="mentee-section">Current Students <span class="sec-count">{{ current_students.size }}</span></h2>

<div class="mentee-cards">
{% assign current_sorted = current_students | sort: "end_year" %}
{% for s in current_sorted %}{% assign target = s.website | default: s.url %}
  {% assign dept = s.department %}{% assign coadv = "" %}
  {% if dept contains "co-advised with" %}{% assign parts = dept | split: "(co-advised with " %}{% assign dept = parts[0] | strip %}{% assign coadv = parts[1] | replace: ")", "" | strip %}{% endif %}
  <div class="mcard">
    <div class="mcard-body">
      <h3>{% if s.website and s.website != "" %}<a href="{{ s.website }}">{{ s.title }}</a>{% else %}{{ s.title }}{% endif %}</h3>
      <div class="mcard-meta">{{ dept }}</div>
      <span class="mcard-year">Expected {{ s.end_year | replace: " (expected)", "" }}</span>
      {% if coadv != "" %}<div class="mcard-co">co-advised with {{ coadv }}</div>{% endif %}
    </div>
  </div>
{% endfor %}
</div>

<!-- ============ ALUMNI ============ -->
<h2 class="mentee-section">Alumni <span class="sec-count">{{ all_alumni.size }}</span></h2>

<h3 id="phd-graduates" class="mentee-group">PhD Graduates <span class="gc">{{ phd_alumni.size }}</span></h3>
{% assign phd_sorted = phd_alumni | sort: "end_year" | reverse %}
{% for a in phd_sorted %}<div class="mentee-row">
  <div class="mr-top"><span class="mr-name">{% if a.website and a.website != "" %}<a href="{{ a.website }}">{{ a.title }}</a>{% else %}{{ a.title }}{% endif %}</span><span class="mr-year">{{ a.end_year }}</span></div>
  {% if a.thesis_title and a.thesis_title != "" %}<div class="mr-thesis">&ldquo;{{ a.thesis_title }}&rdquo;</div>{% endif %}
  <div class="mr-meta">{% if a.current_position and a.current_position != "" %}<span class="mr-pos">{{ a.current_position }}</span>{% if a.department and a.department != "" %} &middot; {% endif %}{% endif %}{{ a.department }}{% if a.awards and a.awards != "" %} &middot; <em>{{ a.awards }}</em>{% endif %}</div>
</div>
{% endfor %}

<h3 id="postdocs" class="mentee-group">Postdocs <span class="gc">{{ postdoc_alumni.size }}</span></h3>
{% assign post_sorted = postdoc_alumni | sort: "end_year" | reverse %}
{% for a in post_sorted %}<div class="mentee-row">
  <div class="mr-top"><span class="mr-name">{% if a.website and a.website != "" %}<a href="{{ a.website }}">{{ a.title }}</a>{% else %}{{ a.title }}{% endif %}</span><span class="mr-year">{% if a.start_year and a.start_year != "" %}{{ a.start_year }}&ndash;{% endif %}{{ a.end_year }}</span></div>
  <div class="mr-meta">{% if a.current_position and a.current_position != "" %}<span class="mr-pos">{{ a.current_position }}</span>{% if a.department and a.department != "" %} &middot; {% endif %}{% endif %}{{ a.department }}</div>
</div>
{% endfor %}

<h3 id="masters-students" class="mentee-group">Master&rsquo;s Students <span class="gc">{{ masters_alumni.size }}</span></h3>
{% assign ms_sorted = masters_alumni | sort: "end_year" | reverse %}
{% for a in ms_sorted %}<div class="mentee-row">
  <div class="mr-top"><span class="mr-name">{% if a.website and a.website != "" %}<a href="{{ a.website }}">{{ a.title }}</a>{% else %}{{ a.title }}{% endif %}</span><span class="mr-year">{{ a.end_year }}</span></div>
  {% if a.thesis_title and a.thesis_title != "" %}<div class="mr-thesis">&ldquo;{{ a.thesis_title }}&rdquo;</div>{% endif %}
  <div class="mr-meta">{% if a.current_position and a.current_position != "" %}<span class="mr-pos">{{ a.current_position }}</span>{% if a.department and a.department != "" %} &middot; {% endif %}{% endif %}{{ a.department }}</div>
</div>
{% endfor %}

<h3 id="undergraduate-researchers" class="mentee-group">Undergraduate Researchers <span class="gc">{{ undergrad_alumni.size }}</span></h3>
{% assign ug_sorted = undergrad_alumni | sort: "end_year" | reverse %}
{% for a in ug_sorted %}<div class="mentee-row">
  <div class="mr-top"><span class="mr-name">{% if a.website and a.website != "" %}<a href="{{ a.website }}">{{ a.title }}</a>{% else %}{{ a.title }}{% endif %}</span><span class="mr-year">{{ a.end_year }}</span></div>
  {% if a.thesis_title and a.thesis_title != "" %}<div class="mr-thesis">&ldquo;{{ a.thesis_title }}&rdquo;</div>{% endif %}
  <div class="mr-meta">{% if a.current_position and a.current_position != "" %}<span class="mr-pos">{{ a.current_position }}</span>{% if a.department and a.department != "" %} &middot; {% endif %}{% endif %}{{ a.department }}</div>
</div>
{% endfor %}
