---
layout: page
permalink: /team/
title: Team
description: Over the years, I’ve had the pleasure of supervising and working with some wonderful people.
nav: true
nav_order: 2
---

{% assign present_members = site.data.team | where: 'status', 'present' %}
{% assign former_members = site.data.team | where: 'status', 'former' | sort: 'end' | reverse %}

<section class="team-section" aria-labelledby="present-members">
  <h2 id="present-members">Present members</h2>
  <div class="team-grid">
    {% for member in present_members %}
      {% include team-member.html member=member %}
    {% endfor %}
  </div>
</section>

<section class="team-section former-section" aria-labelledby="former-members">
  <h2 id="former-members">Past members</h2>
  <ul class="former-list">
    {% for member in former_members %}
    <li>
      <div class="former-person">
        <strong>{{ member.name | escape }}</strong>
        <span class="former-dates">{% if member.role == 'PhD Researcher' %}PhD{% else %}{{ member.role | escape }}{% endif %} · {% if member.end %}{{ member.start }}–{{ member.end }}{% else %}Joined {{ member.start }}{% endif %}</span>
      </div>
      <p>{{ member.project | escape }}</p>
      {% if member.affiliation %}
      <p class="member-affiliation">Part of {{ member.affiliation | escape }}</p>
      {% endif %}
      {% if member.profile_url %}
      <a class="member-profile" href="{{ member.profile_url | escape }}" aria-label="{{ member.name | escape }}: {{ member.profile_label | escape }}">{{ member.profile_label | escape }}</a>
      {% endif %}
    </li>
    {% endfor %}
  </ul>
</section>
