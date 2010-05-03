<html>
<form action="/" method="get">
<input type="text" name="postcode" />
<input type="submit" />
</form>
{% if postcode %}
<p>
	The postcode: {{ postcode.postcode }}
	is in: {{ postcode.ward.name }} ({{ postcode.ward.district.name }} - {{postcode.ward.district.county.name}})
</p>
{% endif %}
</html>
