<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Python: module agent</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head><body bgcolor="#f0f0f8">

<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="heading">
<tr bgcolor="#7799ee">
<td valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial">&nbsp;<br><big><big><strong>agent</strong></big></big></font></td
><td align=right valign=bottom
><font color="#ffffff" face="helvetica, arial"><a href=".">index</a><br><a href="file:/Users/jonasgregorio/quaesit/quaesit/agent.py">/Users/jonasgregorio/quaesit/quaesit/agent.py</a></font></td></tr></table>
    <p></p>
<p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#aa55cc">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Modules</strong></big></font></td></tr>
    
<tr><td bgcolor="#aa55cc"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><table width="100%" summary="list"><tr><td width="25%" valign=top><a href="inspect.html">inspect</a><br>
</td><td width="25%" valign=top></td><td width="25%" valign=top></td><td width="25%" valign=top></td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ee77aa">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Classes</strong></big></font></td></tr>
    
<tr><td bgcolor="#ee77aa"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl>
<dt><font face="helvetica, arial"><a href="builtins.html#object">builtins.object</a>
</font></dt><dd>
<dl>
<dt><font face="helvetica, arial"><a href="agent.html#Agent">Agent</a>
</font></dt></dl>
</dd>
</dl>
 <p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ffc8d8">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#000000" face="helvetica, arial"><a name="Agent">class <strong>Agent</strong></a>(<a href="builtins.html#object">builtins.object</a>)</font></td></tr>
    
<tr bgcolor="#ffc8d8"><td rowspan=2><tt>&nbsp;&nbsp;&nbsp;</tt></td>
<td colspan=2><tt><a href="#Agent">Agent</a>(world,&nbsp;coords:&nbsp;Tuple&nbsp;=&nbsp;None)<br>
&nbsp;<br>
Class&nbsp;to&nbsp;represent&nbsp;an&nbsp;agent&nbsp;in&nbsp;an&nbsp;agent-based&nbsp;model.<br>&nbsp;</tt></td></tr>
<tr><td>&nbsp;</td>
<td width="100%">Methods defined here:<br>
<dl><dt><a name="Agent-__init__"><strong>__init__</strong></a>(self, world, coords: Tuple = None)</dt><dd><tt>Initialize&nbsp;self.&nbsp;&nbsp;See&nbsp;help(type(self))&nbsp;for&nbsp;accurate&nbsp;signature.</tt></dd></dl>

<dl><dt><a name="Agent-agents_here"><strong>agents_here</strong></a>(self) -&gt; List</dt><dd><tt>Returns&nbsp;all&nbsp;agents&nbsp;located&nbsp;on&nbsp;the&nbsp;same&nbsp;cell&nbsp;as&nbsp;oneself.</tt></dd></dl>

<dl><dt><a name="Agent-agents_in_radius"><strong>agents_in_radius</strong></a>(self, radius: int)</dt><dd><tt>Returns&nbsp;all&nbsp;agents&nbsp;within&nbsp;a&nbsp;distance&nbsp;of&nbsp;oneself.</tt></dd></dl>

<dl><dt><a name="Agent-cell_here"><strong>cell_here</strong></a>(self, layer=None)</dt><dd><tt>Returns&nbsp;the&nbsp;value&nbsp;of&nbsp;a&nbsp;layer&nbsp;in&nbsp;the&nbsp;model's&nbsp;grid&nbsp;for&nbsp;the&nbsp;cell<br>
where&nbsp;the&nbsp;agent&nbsp;is.&nbsp;If&nbsp;no&nbsp;layer&nbsp;is&nbsp;specified,&nbsp;the&nbsp;values&nbsp;of&nbsp;all<br>
layers&nbsp;are&nbsp;returned.</tt></dd></dl>

<dl><dt><a name="Agent-cells_in_radius"><strong>cells_in_radius</strong></a>(self, radius: int) -&gt; Dict</dt><dd><tt>Returns&nbsp;all&nbsp;cells&nbsp;and&nbsp;respective&nbsp;attributes&nbsp;within&nbsp;a&nbsp;distance<br>
of&nbsp;the&nbsp;agent.</tt></dd></dl>

<dl><dt><a name="Agent-die"><strong>die</strong></a>(self)</dt><dd><tt>Remove&nbsp;the&nbsp;agent&nbsp;from&nbsp;the&nbsp;world.</tt></dd></dl>

<dl><dt><a name="Agent-empty_cells_in_radius"><strong>empty_cells_in_radius</strong></a>(self, radius: int) -&gt; Dict</dt><dd><tt>Returns&nbsp;all&nbsp;empty&nbsp;cells&nbsp;(with&nbsp;no&nbsp;agents&nbsp;on&nbsp;them)&nbsp;and&nbsp;respective<br>
attributes&nbsp;within&nbsp;a&nbsp;distance&nbsp;of&nbsp;the&nbsp;agent.</tt></dd></dl>

<dl><dt><a name="Agent-face_towards"><strong>face_towards</strong></a>(self, coords: Tuple)</dt><dd><tt>Turns&nbsp;the&nbsp;agent's&nbsp;direction&nbsp;towards&nbsp;a&nbsp;given&nbsp;pair&nbsp;of&nbsp;coordinates.</tt></dd></dl>

<dl><dt><a name="Agent-forward"><strong>forward</strong></a>(self, n_steps: int = 1)</dt><dd><tt>Moves&nbsp;the&nbsp;agent&nbsp;a&nbsp;number&nbsp;of&nbsp;cells&nbsp;forward&nbsp;in&nbsp;the&nbsp;direction&nbsp;it<br>
is&nbsp;currently&nbsp;facing.</tt></dd></dl>

<dl><dt><a name="Agent-get_distance"><strong>get_distance</strong></a>(self, coords: Tuple) -&gt; int</dt><dd><tt>Returns&nbsp;the&nbsp;distance&nbsp;(in&nbsp;cells)&nbsp;from&nbsp;the&nbsp;agent&nbsp;to&nbsp;a&nbsp;pair&nbsp;of<br>
coordinates.</tt></dd></dl>

<dl><dt><a name="Agent-hatch"><strong>hatch</strong></a>(self)</dt><dd><tt>Creates&nbsp;an&nbsp;agent&nbsp;and&nbsp;initializes&nbsp;it&nbsp;with&nbsp;the&nbsp;same&nbsp;parameters&nbsp;as<br>
oneself.</tt></dd></dl>

<dl><dt><a name="Agent-move_to"><strong>move_to</strong></a>(self, coords: Tuple)</dt><dd><tt>Places&nbsp;the&nbsp;agent&nbsp;in&nbsp;a&nbsp;different&nbsp;cell&nbsp;of&nbsp;the&nbsp;world&nbsp;grid.</tt></dd></dl>

<dl><dt><a name="Agent-nearest_agent"><strong>nearest_agent</strong></a>(self, agents: List = None)</dt><dd><tt>Given&nbsp;a&nbsp;list&nbsp;of&nbsp;agents,&nbsp;returns&nbsp;the&nbsp;agent&nbsp;that&nbsp;is&nbsp;nearest&nbsp;to<br>
oneself.&nbsp;If&nbsp;no&nbsp;list&nbsp;is&nbsp;provided,&nbsp;all&nbsp;agents&nbsp;are&nbsp;evaluated.</tt></dd></dl>

<dl><dt><a name="Agent-nearest_cell"><strong>nearest_cell</strong></a>(self, cells: Union[List, Dict]) -&gt; Tuple</dt><dd><tt>Given&nbsp;a&nbsp;list&nbsp;or&nbsp;dictionary&nbsp;of&nbsp;cells,&nbsp;returns&nbsp;the&nbsp;coordinates&nbsp;of<br>
the&nbsp;cell&nbsp;that&nbsp;is&nbsp;nearest&nbsp;to&nbsp;the&nbsp;agent.</tt></dd></dl>

<dl><dt><a name="Agent-random_walk"><strong>random_walk</strong></a>(self, n_steps: int = 1)</dt><dd><tt>Moves&nbsp;the&nbsp;agent&nbsp;one&nbsp;cell&nbsp;forward&nbsp;in&nbsp;a&nbsp;random&nbsp;direction&nbsp;for&nbsp;a<br>
number&nbsp;of&nbsp;times.</tt></dd></dl>

<dl><dt><a name="Agent-step"><strong>step</strong></a>(self)</dt><dd><tt>Methods&nbsp;to&nbsp;be&nbsp;performed&nbsp;by&nbsp;the&nbsp;agent&nbsp;at&nbsp;each&nbsp;step&nbsp;of&nbsp;the<br>
simulation.</tt></dd></dl>

<dl><dt><a name="Agent-turn_left"><strong>turn_left</strong></a>(self, angle: int = 90)</dt><dd><tt>Rotates&nbsp;the&nbsp;agent's&nbsp;direction&nbsp;a&nbsp;number&nbsp;of&nbsp;degrees&nbsp;to&nbsp;the&nbsp;left.</tt></dd></dl>

<dl><dt><a name="Agent-turn_right"><strong>turn_right</strong></a>(self, angle: int = 90)</dt><dd><tt>Rotates&nbsp;the&nbsp;agent's&nbsp;direction&nbsp;a&nbsp;number&nbsp;of&nbsp;degrees&nbsp;to&nbsp;the&nbsp;right.</tt></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<hr>
Data and other attributes defined here:<br>
<dl><dt><strong>__abstractmethods__</strong> = frozenset({'step'})</dl>

<dl><dt><strong>colors</strong> = ['blue', 'brown', 'cyan', 'gray', 'green', 'magenta', 'orange', 'pink', 'purple', 'red', 'yellow']</dl>

</td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#eeaa77">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Functions</strong></big></font></td></tr>
    
<tr><td bgcolor="#eeaa77"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl><dt><a name="-asin"><strong>asin</strong></a>(x, /)</dt><dd><tt>Return&nbsp;the&nbsp;arc&nbsp;sine&nbsp;(measured&nbsp;in&nbsp;radians)&nbsp;of&nbsp;x.</tt></dd></dl>
 <dl><dt><a name="-cos"><strong>cos</strong></a>(x, /)</dt><dd><tt>Return&nbsp;the&nbsp;cosine&nbsp;of&nbsp;x&nbsp;(measured&nbsp;in&nbsp;radians).</tt></dd></dl>
 <dl><dt><a name="-degrees"><strong>degrees</strong></a>(x, /)</dt><dd><tt>Convert&nbsp;angle&nbsp;x&nbsp;from&nbsp;radians&nbsp;to&nbsp;degrees.</tt></dd></dl>
 <dl><dt><a name="-hypot"><strong>hypot</strong></a>(x, y, /)</dt><dd><tt>Return&nbsp;the&nbsp;Euclidean&nbsp;distance,&nbsp;sqrt(x*x&nbsp;+&nbsp;y*y).</tt></dd></dl>
 <dl><dt><a name="-radians"><strong>radians</strong></a>(x, /)</dt><dd><tt>Convert&nbsp;angle&nbsp;x&nbsp;from&nbsp;degrees&nbsp;to&nbsp;radians.</tt></dd></dl>
 <dl><dt><a name="-sin"><strong>sin</strong></a>(x, /)</dt><dd><tt>Return&nbsp;the&nbsp;sine&nbsp;of&nbsp;x&nbsp;(measured&nbsp;in&nbsp;radians).</tt></dd></dl>
</td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#55aa55">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Data</strong></big></font></td></tr>
    
<tr><td bgcolor="#55aa55"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><strong>Dict</strong> = typing.Dict<br>
<strong>List</strong> = typing.List<br>
<strong>Tuple</strong> = typing.Tuple<br>
<strong>Union</strong> = typing.Union</td></tr></table>
</body></html>