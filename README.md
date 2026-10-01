# Vladimir V. Gusev — personal website

A small Jekyll/al-folio site containing About, Team, and a custom 404 page.

## Editing

Work on the `source` branch. Edit `_pages/about.md` for biography/contact layout,
`_data/team.json` for present and former members, `_config.yml` for site settings, and `_sass/` for styles. The former `master`
branch contains historical generated output; do not edit that HTML.

The research paragraphs are unchanged by the cleanup. Teaching, CV, sample
publications, projects, news, blog posts, and the external sample feed have been
removed. Their history remains in Git.

## Local preview and verification

Use Ruby 3.3, Bundler, and Python 3:

```sh
bundle install
bash bin/build
bundle exec jekyll serve
```

Open http://localhost:4000. `bin/build` cleans the output before building and
checks local links, fragment links, and the absence of obsolete pages. The output
is `_site/` and is not committed. Responsive portraits are stored in `assets/img/`;
ImageMagick is not required. Replace all portrait variants together if updating it.

## Publishing

The workflow builds pushes and pull requests targeting `source`. Only pushes to
`source` (or a manual workflow run on `source`) deploy. Pull requests only validate.
It publishes a fresh GitHub Pages artifact; no force-push or generated branch is
needed, and deleted pages cannot linger from previous deployments.

Before the first deployment, set GitHub **Settings → Pages → Build and deployment
→ Source** to **GitHub Actions**. If the `github-pages` environment restricts
branches, allow `source`. Preserve the custom domain `www.vlgusev.co.uk` and HTTPS in
Pages settings. These account settings are not changed by local edits.

The old `bin/deploy` script was removed because it deleted files and force-pushed
branches. Commit and push the reviewed `source` changes to publish with the workflow.

Theme: [al-folio](https://github.com/alshedivat/al-folio), under the included MIT license.

## CV import

Team profiles were prefilled from `../CV_ongoing/cv_promo.tex`, using its active
PhD supervision entries. Summer interns were excluded at the site owner’s request. Commented-out entries were excluded.
Open-ended dates are present memberships; explicit end dates are former memberships.
Dannie Ritchie and Abdulatif Cisse were confirmed as former members by the site owner.
Former members’ primary-supervision sequences are retained as recorded in the CV. No completion
qualifications, subsequent jobs, or photos have been inferred.

`_data/team.json` holds 18 editable profiles (5 present, 13 former). To add a
postdoc, use the same fields and change `role`; no template change is needed.
`_data/publications.json` holds 65 CV publication records: 24 journal papers,
28 conference papers, and 13 abstracts/workshop papers. The latter retain the
CV's limited-peer-review marker. These are reference data for future Highlights;
the full publication list is not displayed automatically. The CV itself is not
copied into the published site. The user-confirmed Senior Lecturer title takes
precedence over the CV's older employment title.

The Team page uses cards for present members and a compact list for former members,
with PhD labels, years, and thesis titles. Optional `profile_url` and `profile_label`
fields link to a personal website or LinkedIn profile. Profiles were checked against
research topics and university history on 1 October 2026; personal websites take
priority. Profile links are available for 13 members. No confident match was found for
Dumitru Mirauta, Sam Durdy, Dannie Ritchie, Abdulatif Cisse, or Rio McDade;
these remain unlinked rather than pointing to an unrelated person.

Xingzhi Zhao was removed at the site owner’s request. Stavros Gerolymatos was
confirmed as graduating in 2026 and moved to former members. His final thesis title
is taken from the [University of Liverpool repository](https://livrepository.liverpool.ac.uk/3198939/),
replacing the earlier project title from the CV.

See [the PhD title audit](scripts/team-title-audit.md) for university sources,
unverified titles, and differences between current project descriptions.

Elena Zamaraeva is a former postdoctoral researcher at the Leverhulme Research
Centre for Functional Materials Design, September 2020–June 2025, confirmed
by the LinkedIn screenshot supplied by the owner. The site displays 2020–2025
to match the year-only format used for other members. Present cards omit
primary-supervision credits; Emma’s joint collaborators use the `joint_with` field.

Esma Kurban was added as a present Postdoctoral Research Fellow, starting
September 2025. Her role, start date and research description come from the
LinkedIn screenshot supplied by the owner; the site displays 2025–present.

Esma’s affiliation is displayed as plain text: AIchemy — AI for Chemistry Hub.
Reference website: https://aichemy.ac.uk/.
The [hub team page](https://aichemy.ac.uk/the-team/) confirms her September 2025
start and crystal structure prediction research for materials discovery.

Elena’s concise research description is based on [Reinforcement learning in crystal
structure prediction (2023)](https://pubs.rsc.org/en/content/articlelanding/2023/dd/d3dd00063j)
and [MACS (June 2025)](https://arxiv.org/abs/2506.04195). Her Leverhulme affiliation
is retained separately below the description.

## Research artwork

The About footer artwork uses the owner-supplied `Nature_cover_landscape.jpg`, copied
unchanged to `assets/img/research-landscape.jpg`. The banner loads responsive
960px or 1920px WebP versions (quality 82), with lazy loading. Click the banner to
view the original full artwork. Its navy, cyan and magenta palette informs both colour themes;
`_sass/_artwork.scss` controls the framing and fades. Social links sit above
the artwork, which blends into the page background and copyright footer. Original references remain outside
the published site.
