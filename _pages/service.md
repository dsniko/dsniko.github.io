---
layout: archive
title: "Service"
permalink: /service/
author_profile: true

---

{% assign sorted = site.service | sort: 'start' | reverse %}
<ul>
  {% for item in sorted %}
    <li><strong>{{ item.role }}:</strong> {{ item.organization }} ({{ item.start }} – {{ item.end }})</li>
  {% endfor %}
</ul>
