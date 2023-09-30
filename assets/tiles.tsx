<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.10" tiledversion="1.10.2" name="tiles" tilewidth="8" tileheight="8" tilecount="40" columns="8">
 <image source="tiles.png" width="64" height="40"/>
 <tile id="0">
  <animation>
   <frame tileid="0" duration="100"/>
   <frame tileid="1" duration="100"/>
   <frame tileid="2" duration="100"/>
   <frame tileid="3" duration="100"/>
  </animation>
 </tile>
 <tile id="4">
  <animation>
   <frame tileid="4" duration="100"/>
   <frame tileid="5" duration="100"/>
   <frame tileid="6" duration="100"/>
   <frame tileid="7" duration="100"/>
  </animation>
 </tile>
 <tile id="16">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <tile id="17">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <tile id="24">
  <properties>
   <property name="direction" value="0"/>
   <property name="product" value="cross"/>
   <property name="type" value="dest"/>
  </properties>
 </tile>
 <tile id="25">
  <properties>
   <property name="direction" value="1"/>
   <property name="product" value="cross"/>
   <property name="type" value="dest"/>
  </properties>
 </tile>
 <tile id="26">
  <properties>
   <property name="direction" value="2"/>
   <property name="product" value="cross"/>
   <property name="type" value="dest"/>
  </properties>
 </tile>
 <tile id="27">
  <properties>
   <property name="direction" value="3"/>
   <property name="product" value="cross"/>
   <property name="type" value="dest"/>
  </properties>
 </tile>
 <tile id="28">
  <properties>
   <property name="direction" value="0"/>
   <property name="product" value="cross"/>
   <property name="type" value="source"/>
  </properties>
 </tile>
 <tile id="29">
  <properties>
   <property name="direction" value="1"/>
   <property name="product" value="cross"/>
   <property name="type" value="source"/>
  </properties>
 </tile>
 <tile id="30">
  <properties>
   <property name="direction" value="2"/>
   <property name="product" value="cross"/>
   <property name="type" value="source"/>
  </properties>
 </tile>
 <tile id="31">
  <properties>
   <property name="direction" value="3"/>
   <property name="product" value="cross"/>
   <property name="type" value="source"/>
  </properties>
 </tile>
 <wangsets>
  <wangset name="brique" type="corner" tile="-1">
   <wangcolor name="" color="#ff0000" tile="-1" probability="1"/>
   <wangtile tileid="16" wangid="0,0,0,1,0,1,0,0"/>
   <wangtile tileid="17" wangid="0,0,0,1,0,1,0,1"/>
  </wangset>
 </wangsets>
</tileset>
