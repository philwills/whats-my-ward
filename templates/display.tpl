<html>
<form action="/" method="get">
<input type="text" name="postcode" />
<input type="submit" />
</form>
{% if postcode %}
<ul>
	<li>Postcode: {{ postcode.postcode }}</li>
	<li>Ward: {{ postcode.ward.name }} ({{ postcode.ward.district.name }} - {{postcode.ward.district.county.name}})</li>
</ul>
{% endif %}
</html>
