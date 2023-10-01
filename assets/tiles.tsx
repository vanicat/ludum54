<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.10" tiledversion="1.10.2" name="tiles" tilewidth="8" tileheight="8" tilecount="48" columns="8">
 <image source="tiles.png" width="64" height="48"/>
 <tile id="0">
  <properties>
   <property name="bottom" value="in"/>
   <property name="left" value="None"/>
   <property name="right" value="None"/>
   <property name="top" value="out"/>
  </properties>
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
   <property name="direction" type="int" value="0"/>
   <property name="product" value="cross"/>
   <property name="type" value="dest"/>
  </properties>
 </tile>
 <tile id="25">
  <properties>
   <property name="direction" type="int" value="1"/>
   <property name="product" value="cross"/>
   <property name="type" value="dest"/>
  </properties>
 </tile>
 <tile id="26">
  <properties>
   <property name="direction" type="int" value="2"/>
   <property name="product" value="cross"/>
   <property name="type" value="dest"/>
  </properties>
 </tile>
 <tile id="27">
  <properties>
   <property name="direction" type="int" value="3"/>
   <property name="product" value="cross"/>
   <property name="type" value="dest"/>
  </properties>
 </tile>
 <tile id="28">
  <properties>
   <property name="direction" type="int" value="0"/>
   <property name="product" value="cross"/>
   <property name="type" value="source"/>
  </properties>
 </tile>
 <tile id="29">
  <properties>
   <property name="direction" type="int" value="1"/>
   <property name="product" value="cross"/>
   <property name="type" value="source"/>
  </properties>
 </tile>
 <tile id="30">
  <properties>
   <property name="direction" type="int" value="2"/>
   <property name="product" value="cross"/>
   <property name="type" value="source"/>
  </properties>
 </tile>
 <tile id="31">
  <properties>
   <property name="direction" type="int" value="3"/>
   <property name="product" value="cross"/>
   <property name="type" value="source"/>
  </properties>
 </tile>
 <tile id="33">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <tile id="34">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <tile id="35">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <tile id="36">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <tile id="37">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <tile id="38">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <tile id="39">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <tile id="40">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <tile id="41">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <tile id="42">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <tile id="43">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <tile id="44">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <tile id="45">
  <properties>
   <property name="type" value="wall"/>
  </properties>
 </tile>
 <wangsets>
  <wangset name="Jeu de Tuiles Sans Nom" type="mixed" tile="33">
   <wangcolor name="" color="#ff0000" tile="-1" probability="1"/>
   <wangtile tileid="33" wangid="1,1,1,1,1,1,1,1"/>
   <wangtile tileid="34" wangid="0,0,1,1,1,0,0,0"/>
   <wangtile tileid="35" wangid="0,0,1,1,1,1,1,0"/>
   <wangtile tileid="36" wangid="0,0,0,0,1,1,1,0"/>
   <wangtile tileid="37" wangid="1,1,1,1,1,0,0,0"/>
   <wangtile tileid="38" wangid="0,0,0,0,0,1,1,1"/>
   <wangtile tileid="39" wangid="1,1,1,0,0,0,0,0"/>
   <wangtile tileid="40" wangid="1,1,1,0,0,0,1,1"/>
   <wangtile tileid="41" wangid="1,0,0,0,0,0,1,1"/>
   <wangtile tileid="42" wangid="1,1,1,1,1,1,1,0"/>
   <wangtile tileid="43" wangid="1,1,1,0,1,1,1,1"/>
   <wangtile tileid="44" wangid="1,1,1,1,1,0,1,1"/>
   <wangtile tileid="45" wangid="1,0,1,1,1,1,1,1"/>
  </wangset>
 </wangsets>
</tileset>
