---
layout: page
title: "Service"
permalink: /service/
---

{% assign sorted = site.service | sort: 'start' | reverse %}
<ul>
  {% for item in sorted %}
    <li><strong>{{ item.role }}:</strong> {{ item.organization }} ({{ item.start }} – {{ item.end }})</li>
  {% endfor %}
</ul>
