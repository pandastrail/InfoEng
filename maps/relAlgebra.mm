<map version="freeplane 1.5.9">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node FOLDED="false" ID="ID_437908838" CREATED="1505213359803" MODIFIED="1505213564693" STYLE="oval"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <b>Relationale Algebra </b>
    </p>
    <p>
      <font color="#0000ff">(Relational Algebra)</font>
    </p>
  </body>
</html>
</richcontent>
<hook NAME="MapStyle" zoom="0.909">
    <conditional_styles>
        <conditional_style ACTIVE="true" LOCALIZED_STYLE_REF="styles.connection" LAST="false">
            <node_periodic_level_condition PERIOD="2" REMAINDER="1"/>
        </conditional_style>
        <conditional_style ACTIVE="true" LOCALIZED_STYLE_REF="styles.topic" LAST="false">
            <node_level_condition VALUE="2" MATCH_CASE="false" MATCH_APPROXIMATELY="false" COMPARATION_RESULT="0" SUCCEED="true"/>
        </conditional_style>
        <conditional_style ACTIVE="true" LOCALIZED_STYLE_REF="styles.subtopic" LAST="false">
            <node_level_condition VALUE="4" MATCH_CASE="false" MATCH_APPROXIMATELY="false" COMPARATION_RESULT="0" SUCCEED="true"/>
        </conditional_style>
        <conditional_style ACTIVE="true" LOCALIZED_STYLE_REF="styles.subsubtopic" LAST="false">
            <node_level_condition VALUE="6" MATCH_CASE="false" MATCH_APPROXIMATELY="false" COMPARATION_RESULT="0" SUCCEED="true"/>
        </conditional_style>
    </conditional_styles>
    <properties fit_to_viewport="false;" show_note_icons="true" show_icon_for_attributes="true"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" COLOR="#000000" STYLE="fork">
<font NAME="Arial" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.connection" COLOR="#606060" STYLE="fork">
<font NAME="Arial" SIZE="8" BOLD="false"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
</stylenode>
</stylenode>
</map_styles>
</hook>
<richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      by Edgar F. Codd at IBM
    </p>
    <p>
      Provides theoretical foundation for relational databases
    </p>
  </body>
</html>
</richcontent>
<node TEXT="Operator" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" POSITION="right" ID="ID_1890580342" CREATED="1505213615125" MODIFIED="1505213752580"><richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Symbole
    </p>
    <p>
      Representan procedimientos
    </p>
  </body>
</html>
</richcontent>
<node TEXT="Funktionen (in Datenbank)" ID="ID_1424775661" CREATED="1505213878474" MODIFIED="1505213888480"/>
<node LOCALIZED_STYLE_REF="AutomaticLayout.level,3" ID="ID_1026378683" CREATED="1505317515840" MODIFIED="1505400489867"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p style="text-align: center">
      Projection (<font face="Nimbus Roman No9 L, Times New Roman, Times, serif" size="19.824px">&#960;</font>)
    </p>
    <p style="text-align: center">
      <font size="2" color="#3300cc">(Projektion)</font>
    </p>
  </body>
</html>

</richcontent>
<node TEXT="unary operation; result is a set when all tuples in R are restricted to set" LOCALIZED_STYLE_REF="AutomaticLayout.level,4" ID="ID_1654913886" CREATED="1505400870267" MODIFIED="1505402107083">
<hook EQUATION="\Pi_a_1,...,a_n(R) \text{ where } a_1,...a_n \text{ is a set of attribute names}" NAME="plugins/latex/LatexNodeHook.properties"/>
<node TEXT="ex. given R4 a b c&#xa;                     1 2 2&#xa;                     1 2 3" LOCALIZED_STYLE_REF="AutomaticLayout.level,4" ID="ID_805306389" CREATED="1505318947180" MODIFIED="1505400286231">
<node LOCALIZED_STYLE_REF="AutomaticLayout.level,4" ID="ID_1080917807" CREATED="1505318994729" MODIFIED="1505319149701"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      get <font size="5">&#960;</font>a,b(R4)
    </p>
  </body>
</html>
</richcontent>
<node TEXT="a b&#xa;1 2" ID="ID_1844972320" CREATED="1505319026583" MODIFIED="1505319102421"/>
</node>
</node>
</node>
<node TEXT="Es k&#xf6;nnen Duplikate entstehen!" ID="ID_1851093989" CREATED="1505400539900" MODIFIED="1505400623370">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node LOCALIZED_STYLE_REF="AutomaticLayout.level,3" ID="ID_892198113" CREATED="1505317877289" MODIFIED="1505400467298"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p style="text-align: center">
      Selection (<i>&#963;)</i>&#160;
    </p>
    <p style="text-align: center">
      <font color="#3300cc" size="2">(Selektion)</font>
    </p>
  </body>
</html>

</richcontent>
<node TEXT="generalized selection is a unary operation" LOCALIZED_STYLE_REF="AutomaticLayout.level,4" ID="ID_939051989" CREATED="1505402074518" MODIFIED="1505402463086">
<hook EQUATION="\sigma_\phi(R) \text{ where } \phi \text{ is a propositional formula with logical operators }&#xa;\wedge \text{ (and), } \vee \text{ (or), and } \neg \text{ negation } " NAME="plugins/latex/LatexNodeHook.properties"/>
<node TEXT="ex. given R1 a b c&#xa;                     1 1 1&#xa;                     1 2 2&#xa;                     2 0 2" LOCALIZED_STYLE_REF="styles.connection" ID="ID_837901840" CREATED="1505318625880" MODIFIED="1505318748930">
<node LOCALIZED_STYLE_REF="AutomaticLayout.level,4" ID="ID_223086262" CREATED="1505318752904" MODIFIED="1505319141582"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      get <i><font size="5">&#963;</font></i>(b=2) &#61658; (c=2)(R1)
    </p>
  </body>
</html>
</richcontent>
<node TEXT="a b c&#xa;1 2 2&#xa;2 0 2" ID="ID_1410409110" CREATED="1505318806581" MODIFIED="1505318828837"/>
</node>
</node>
</node>
</node>
<node TEXT="Rename (&#x3c1;)" LOCALIZED_STYLE_REF="AutomaticLayout.level,3" ID="ID_170428788" CREATED="1505318069275" MODIFIED="1505318142137"/>
<node TEXT="Natural join (&#x22c8;)" LOCALIZED_STYLE_REF="AutomaticLayout.level,3" ID="ID_638067193" CREATED="1505318075748" MODIFIED="1505318143335">
<node TEXT="" ID="ID_1821023861" CREATED="1505319222354" MODIFIED="1505319234099">
<hook URI="file:////infsfi1003/KSAUser01$/ksagilop/home/Downloads/temp/join.jpg" SIZE="0.7853403" NAME="ExternalObject"/>
<node TEXT="ex. given R1 a b c&#xa;                     1 1 1&#xa;                     1 2 2&#xa;                     2 0 2" LOCALIZED_STYLE_REF="styles.connection" ID="ID_770275955" CREATED="1505319240649" MODIFIED="1505319367110"/>
<node TEXT="R2 a d&#xa;     1 1&#xa;     0 1&#xa;     2 0" LOCALIZED_STYLE_REF="styles.connection" ID="ID_1733079576" CREATED="1505319293925" MODIFIED="1505319368665"/>
<node TEXT="R3 c d e&#xa;     1 1 0&#xa;     0 1 1&#xa;     2 1 0&#xa;     2 2 1" LOCALIZED_STYLE_REF="styles.connection" ID="ID_1601844458" CREATED="1505319321092" MODIFIED="1505319370016">
<node LOCALIZED_STYLE_REF="AutomaticLayout.level,4" ID="ID_129117624" CREATED="1505319371720" MODIFIED="1505319441077"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      get R1<font size="5">&#160;&#8904;</font>&#160;(R2 <font size="5">&#8904;</font>&#160;R3)
    </p>
  </body>
</html>
</richcontent>
<node TEXT="First R2 &#x22c8; R3) a c d e&#xa;                        1 1 1 0&#xa;                        1 0 1 1&#xa;                        1 2 1 0&#xa;                        0 1 1 0&#xa;                        0 0 1 1&#xa;                        0 2 1 0" ID="ID_1709332902" CREATED="1505400105531" MODIFIED="1505400201582">
<node TEXT="And then R1 &#x22c8; (R2 &#x22c8; R3) a b c d e&#xa;                                            1 1 1 1 0&#xa;                                            1 2 2 1 0" ID="ID_1824990554" CREATED="1505400203361" MODIFIED="1505400271847"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT=" Union (&#x222a;)" LOCALIZED_STYLE_REF="AutomaticLayout.level,3" ID="ID_1575866033" CREATED="1505318129520" MODIFIED="1505318144550"/>
</node>
<node TEXT="Operand" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" POSITION="left" ID="ID_1965625526" CREATED="1505213681060" MODIFIED="1505213804769"><richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Variable o Valor
    </p>
    <p>
      Variablen oder Werte
    </p>
    <p>
      ...que pueden generar otro valor
    </p>
  </body>
</html>
</richcontent>
<node TEXT="Relationen (in Datenbank)" ID="ID_1773438049" CREATED="1505213833284" MODIFIED="1505213847367"/>
</node>
</node>
</map>
