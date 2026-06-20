---
layout: archive
title: "Mentees"
permalink: /mentees/
author_profile: true
---

{% assign current_students = site.mentees | where: "status", "current" %}
{% assign phd_alumni = site.mentees | where: "status", "alumni" | where: "category", "phd" %}
{% assign postdoc_alumni = site.mentees | where: "status", "alumni" | where: "category", "postdoc" %}
{% assign masters_alumni = site.mentees | where: "status", "alumni" | where: "category", "masters" %}
{% assign undergrad_alumni = site.mentees | where: "status", "alumni" | where: "category", "undergrad" %}

**Quick navigation:**
[Current Students ({{ current_students.size }})](#current-students) ·
[PhD Graduates ({{ phd_alumni.size }})](#phd-graduates) ·
[Postdocs ({{ postdoc_alumni.size }})](#postdocs) ·
[Master's Students ({{ masters_alumni.size }})](#masters-students) ·
[Undergraduate Researchers ({{ undergrad_alumni.size }})](#undergraduate-researchers)

## Current Students

{% assign current_students = site.mentees | where: "status", "current" | sort: "end_year" | reverse %}
{% for student in current_students %}{% assign target = student.website | default: student.url %}**[{{ student.title }}]({{ target }})**  
{% case student.category -%}
  {%- when "phd" -%}PhD Student
  {%- when "postdoc" -%}Postdoc
  {%- when "masters" -%}Master's Student
  {%- when "undergrad" -%}Undergraduate Researcher
  {%- else -%}{{ student.category | capitalize }}
{%- endcase -%}
{%- if student.department and student.department != "" %}, {{ student.department }}{% endif -%}
{%- if student.end_year and student.end_year != "" %}, {{ student.end_year }}{% endif %}

{% endfor %}

## Alumni

### PhD Graduates
{% assign phd_alumni = site.mentees | where: "status", "alumni" | where: "category", "phd" | sort: "end_year" | reverse %}
{% for alumnus in phd_alumni %}{% if alumnus.website and alumnus.website != "" %}**[{{ alumnus.title }}]({{ alumnus.website }})**{% else %}**{{ alumnus.title }}**{% endif %} ({{ alumnus.end_year }})  
{% if alumnus.thesis_title and alumnus.thesis_title != "" %}*Dissertation:* "{{ alumnus.thesis_title }}"  
{% endif %}{% if alumnus.current_position and alumnus.current_position != "" %}*Current Position:* {{ alumnus.current_position }}  
{% endif %}{% if alumnus.department and alumnus.department != "" %}*Department:* {{ alumnus.department }}  
{% endif %}{% if alumnus.awards and alumnus.awards != "" %}*Award:* {{ alumnus.awards }}  
{% endif %}
{% endfor %}

### Postdocs
{% assign postdoc_alumni = site.mentees | where: "status", "alumni" | where: "category", "postdoc" | sort: "end_year" | reverse %}
{% for alumnus in postdoc_alumni %}{% if alumnus.website and alumnus.website != "" %}**[{{ alumnus.title }}]({{ alumnus.website }})**{% else %}**{{ alumnus.title }}**{% endif %} ({% if alumnus.start_year and alumnus.start_year != "" %}{{ alumnus.start_year }}–{% endif %}{{ alumnus.end_year }})  
{% if alumnus.department and alumnus.department != "" %}*Department:* {{ alumnus.department }}  
{% endif %}{% if alumnus.current_position and alumnus.current_position != "" %}*Current Position:* {{ alumnus.current_position }}  
{% endif %}
{% endfor %}

### Master's Students
{% assign masters_alumni = site.mentees | where: "status", "alumni" | where: "category", "masters" | sort: "end_year" | reverse %}
{% for alumnus in masters_alumni %}{% if alumnus.website and alumnus.website != "" %}**[{{ alumnus.title }}]({{ alumnus.website }})**{% else %}**{{ alumnus.title }}**{% endif %} ({{ alumnus.department }}, {{ alumnus.end_year }})  
{% if alumnus.thesis_title and alumnus.thesis_title != "" %}*Thesis:* "{{ alumnus.thesis_title }}"  
{% endif %}{% if alumnus.current_position and alumnus.current_position != "" %}*Current Position:* {{ alumnus.current_position }}  
{% endif %}
{% endfor %}

### Undergraduate Researchers
{% assign undergrad_alumni = site.mentees | where: "status", "alumni" | where: "category", "undergrad" | sort: "end_year" | reverse %}
{% for alumnus in undergrad_alumni %}{% if alumnus.website and alumnus.website != "" %}**[{{ alumnus.title }}]({{ alumnus.website }})**{% else %}**{{ alumnus.title }}**{% endif %} ({{ alumnus.department }}, {{ alumnus.end_year }})  
{% if alumnus.thesis_title and alumnus.thesis_title != "" %}*Thesis:* "{{ alumnus.thesis_title }}"  
{% endif %}{% if alumnus.current_position and alumnus.current_position != "" %}*Current Status:* {{ alumnus.current_position }}  
{% endif %}
{% endfor %}
