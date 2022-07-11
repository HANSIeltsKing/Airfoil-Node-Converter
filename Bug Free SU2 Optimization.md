
# Bug Free SU2
## Adjoint Optimization Error List
<br/>
<br/>

**Cannot set GEO constraints or objectives in unsteady case**
<br/>
If your SU2 is newer than 7.3.0:
<br/>
Open your wrapped config.py
<br/>
delete from:
<br/>
if self.get("TIME_DOMAIN") == "YES":
<br/>
to:
<br/>
self["HISTORY_OUTPUT"]= histFields
<br/>

