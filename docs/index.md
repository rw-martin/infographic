---
title: Windows Virtual Desktop
author: rwmartin
---


# Windows Virtual Desktop Solution
{: .fs-9 }

===

{% include read_time.html %}

===

{{ page.date | date: "%b %d, %Y" }} 

<li> {{ time }} {% if time == '1' %}minute{% else %}minutes{% endif %} minutes to read Contributors: {% avatar rw-martin size=20 %} {% avatar TheOneAndOnlyBillGates size=20 %}


Bespoke solution created to host the C-Log application for the 2020 event based on the Spring WVD release.
{: .fs-4 .fw-600 }


# Solution highlights:
* fslogix profile containers that seamlessly mount at login as virtual disks to aid in keeping login times acceptable.
* Auto scale-out/scale-in automation
* Custom ARM template used to deploy burstable Standard_B2ms
* Optimized Windows 10 Enterprise Multi-Session gold image w/ Office ProPlus and other ready for import into the shared gallery if desired
 


# Dependencies



