---
title: Windows Virtual Desktop
author: rwmartin
---


# Windows Virtual Desktop Solution (WVD)
{: .fs-9 }


{% capture time %}{{ content | reading_time }}{% endcapture %}

09/25/2020 <li> {{ time }} {% if time == '1' %}minute{% else %}minutes{% endif %} minutes to read Contributors: {% avatar rw-martin size=20 %} {% avatar TheOneAndOnlyBillGates size=20 %}


Just the Docs gives your documentation a jumpstart with a responsive Jekyll theme that is easily customizable and hosted on GitHub Pages.
{: .fs-6 .fw-300 }


# Solution highlights:
* fslogix profile containers that seamlessly mount at login as virtual disks to aid in keeping login times acceptable.
* Auto scale-out/scale-in automation
* Custom ARM template used to deploy burstable Standard_B2ms
* Optimized Windows 10 Enterprise Multi-Session gold image w/ Office ProPlus and other ready for import into the shared gallery if desired
 


# Dependencies

Just the Docs is built for [Jekyll](https://jekyllrb.com), a static site generator. View the [quick start guide](https://jekyllrb.com/docs/) for more information. Just the Docs requires no special plugins and can run on GitHub Pages' standard Jekyll compiler. The [Jekyll SEO Tag plugin](https://github.com/jekyll/jekyll-seo-tag) is included by default (no need to run any special installation) to inject SEO and open graph metadata on docs pages. For information on how to configure SEO and open graph metadata visit the [Jekyll SEO Tag usage guide](https://jekyll.github.io/jekyll-seo-tag/usage/).

