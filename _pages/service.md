---
layout: archive
title: "Service"
permalink: /service/
author_profile: true

---

{% assign sorted = site.service | sort: 'start' | reverse %}
<ul>
  {% for item in sorted %}
<li>
  <strong>{{ item.role }}:</strong> {{ item.organization }}
  {% if item.start and item.end %}
    ({{ item.start }} – {{ item.end }})
  {% elsif item.end %}
    ({{ item.end }})
  {% elsif item.start %}
    ({{ item.start }})
  {% endif %}
</li>
  {% endfor %}
</ul>
