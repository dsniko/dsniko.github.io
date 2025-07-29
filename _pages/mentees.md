---
layout: archive
title: "Mentees"
permalink: /mentees/
author_profile: true
---

## Current Students

{% assign current_students = site.mentees | where: "status", "current" | sort: "category" %}
{% for student in current_students %}
[{{ student.title }}]({{ student.url }})  
{% case student.category %}
  {%- when "phd" -%}PhD Student
  {%- when "postdoc" -%}Postdoc
  {%- when "masters" -%}Masters Student
  {%- when "undergrad" -%}Undergraduate Researcher
  {% else %}{{student.category|capitalize}}{% endcase %}
{{ student.department }}{{ student.end_year|default:"Present"}}{{ student.excerpt }}
{% endfor %}

## Alumni

### PhD Graduates
{% assign phd_alumni = site.mentees | where: "status", "alumni" | where: "category", "phd" | sort: "end_year" | reverse %}
{% for alumnus in phd_alumni %}
**[{{ alumnus.title }}]({{ alumnus.website }})** ({{ alumnus.end_year }})
*Dissertation:* "{{ alumnus.thesis_title }}"  
{% if alumnus.current_position %}*Current Position:* {{ alumnus.current_position }}{% endif %}  
{% if alumnus.first_position %}*First Position:* {{ alumnus.first_position }}{% endif %}  
{% if alumnus.department %}*Department:* {{ alumnus.department}}{% endif %}  
{% if alumnus.awards %}*Award:* {{ alumnus.awards }}{% endif %}
{% endfor %}

### Postdocs
{% assign postdoc_alumni = site.mentees | where: "status", "alumni" | where: "category", "postdoc" | sort: "end_year" | reverse %}
{% for alumnus in postdoc_alumni %}
**[{{ alumnus.title }}]({{ alumnus.url }})** ({{ alumnus.end_year }})  
{% if alumnus.current_position %}*Current Position:* {{ alumnus.current_position }}  {% endif %}
{% endfor %}

### Master's Students
{% assign masters_alumni = site.mentees | where: "status", "alumni" | where: "category", "masters" | sort: "end_year" | reverse %}
{% for alumnus in masters_alumni %}
**[{{ alumnus.title }}]({{ alumnus.url }})** ({{ alumnus.end_year }})  
{% if alumnus.thesis_title %}*Thesis:* "{{ alumnus.thesis_title }}"  {% endif %}
{% if alumnus.current_position %}*Current Position:* {{ alumnus.current_position }}  {% endif %}
{% endfor %}

### Undergraduate Researchers
{% assign undergrad_alumni = site.mentees | where: "status", "alumni" | where: "category", "undergrad" | sort: "end_year" | reverse %}
{% for alumnus in undergrad_alumni %}
**[{{ alumnus.title }}]({{ alumnus.url }})** ({{ alumnus.end_year }})  
{% if alumnus.current_position %}*Current Status:* {{ alumnus.current_position }}  {% endif %}
{% endfor %}
