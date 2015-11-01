
**Description**: When possible, use em instead of pix.   
**Source**: [phpied](http://www.phpied.com/css-coding-conventions/), [Moodle](https://docs.moodle.org/dev/CSS_coding_style)  
**Violations**: Usage of unit with value px. For example, the snippet `font-size: 12px;` is a violation. The snippet `font-size: 1em;` does not violate the convention.  
**Actions**: Recognize units with value px  

---
**Description**: Avoid using z-indexes when possible.   
**Source**: [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS)  
**Violations**: Usage of z-index property. Sample violation is the following `z-index: 100;`  
**Actions**: Recognize property with value z-index    
 
---
**Description**: Avoid using !important.   
**Source**: [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS), [Toll](http://www.benjamintoll.com/software/css_code_conventions.html)  
**Violations**: Usage of !important. Sample violation is the following `color: red !important;`  
**Actions**: Recognize usage of !important    

---
**Description**: Do not use id selectors.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-IDs-in-selectors), [Realdeal](http://www.realdealmarketing.net/docs/css-coding-style.php), [Orion](http://wiki.eclipse.org/Orion/Coding_conventions#CSS), [CSS Wizardry](http://csswizardry.com/2012/04/my-html-css-coding-style/), [Moodle](https://docs.moodle.org/dev/CSS_coding_style)  
**Violations**:  Both sources require a warning whenever an id is found. Sample violations are `.mybox #go;`, `#header a` and `#mybox`  
**Actions**: Recognize usage of id selectors   
 
---
**Description**: Disallow @import.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-%40import), [Realdeal](http://www.realdealmarketing.net/docs/css-coding-style.php), [Isobar](http://isobar-idev.github.io/code-standards/), [CodeGuide](http://codeguide.co/)  
**Violations**:  Due to performance reasons, the usage of @import should be avoided. The following pattern is considered a violation `@import url(foo.css);`  
**Actions**: Find usage of @import statements   

---
**Description**: If you must use an id selector (#selector) make sure that you have no more than one in your rule declaration.   
**Source**: [GitHub](http://primercss.io/guidelines/#css)  
**Violations**:  The guideline states that if a selector contains an id, it should not contain any other simple-selectors. Thus, a rule like `#header .search #quicksearch { ... }` is a violation. Note however, that the convention does not apply to multi-selectors, i.e. the following css code is not a violation: `#header, #footer { ... }`  
**Actions**: Recognize selectors and ids; check if selectors with ids contain other simple selectors  
 
---
**Description**: Use rem units preceded by px units for a safe fallback.   
**Source**: [Drupal](https://www.drupal.org/node/1887862)  
**Violations**:  The convention requires declarations with value that uses rem to have a fallback declaration that uses px. The property of the two declarations has to be the same. The following snippet is a violation because the fallback declaration is missing:  
 
```
font-size: 1.5rem;
```
The following snippet is considered ok:
```
font-size: 24px;
font-size: 1.5rem;
```
**Actions**: Recognize declarations, units with value rem, units with value px; find declarations with value that includes rem units; check if a declaration exists immediately before a given declaration; compare property names of declarations; check if the value of declaration contains a px unit.  
 
---
**Description**: CSS files must not include any @charset statements.   
**Source**: [Drupal](https://www.drupal.org/node/1887862)  
**Violations**: Presence of charset at-rule at the beginning of the CSS file: `@charset "UTF-8";`  
**Actions**: Find @charset statements  
 
---
**Description**: Omit the protocol from embedded resources.   
**Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#Protocol)  
**Violations**: Omit the protocol portion (http:, https:) from URLs pointing to images and other media files, style sheets, and scripts unless the respective files are not available over both protocols. Omitting the protocol—which makes the URL relative—prevents mixed content issues and results in minor file size savings. The snippet `url(http://www.google.com/images/example)` is a violation. The snippet `url(//www.google.com/images/example)` is not considered a violation.  
**Actions**: Recognize uri values; check if the value of a uri starts with a given string  
 
---
**Description**: Beware of box model size (rule 1).   
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-IDs-in-selectors)  
**Violations**: In case the ruleset contains the box-sizing property, no warnings are yielded. However, if it does not contain the property, a warning should be issued if any of the following couples of properties are found:
 1. width, border
 2. width, border-left
 3. width, border-right
 4. width, padding
 5. width, padding-left
 6. width, padding-right

**Actions**: Find rulesets that do not contain the box-sizing property; check if they contain the property width and any of the properties in the list [border, border-left, border-right, padding, padding-left, padding-right].  

---
**Description**: Beware of box model size (rule 2).   
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-IDs-in-selectors)  
**Violations**: In case the ruleset contains the box-sizing property, no warnings are yielded. However, if it does not contain the property, a warning should be issued if any of the following couples of properties are found:
 1. height, border
 2. height, border-top
 3. height, border-bottom
 4. height, padding
 5. height, padding-top
 6. height, padding-bottom

**Actions**: Find rulesets that do not contain the box-sizing property; check if they contain the property height and any of the properties in the list [border, border-top, border-bottom, padding, padding-top, padding-bottom].

---
**Description**: Require properties appropriate for display (rule 1).   
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Require-properties-appropriate-for-display)  
**Violations**: A warning is issued when `display: inline` is used with width, height, margin, margin-top, margin-bottom, and float. The following snippet is considered a violation:
 ```
 .mybox {
    display: inline;
    height: 25px;
}
 ```
**Actions**: Recognize rulesets, declarations with specific properties and values; find rulesets containing a declaration with property display and value inline; check if they contain any of the properties on the list [width, height, margin, margin-top, margin-bottom, float]     

---
**Description**: Require properties appropriate for display (rule 2).   
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Require-properties-appropriate-for-display)  
**Violations**: A warning is issued when a ruleset contains a declaration `display: inline-block` and a declaration with property float. The following snippet is considered a violation:
 ```
 .mybox {
    display: inline-block;
    float: left;
}
 ```
**Actions**: Recognize rulesets, declarations with specific properties and values; find rulesets containing a declaration with property display and value inline-block; check if they contain a declaration with property float.     

---
**Description**: Require properties appropriate for display (rule 3).   
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Require-properties-appropriate-for-display)  
**Violations**: A warning is issued when a ruleset contains a declaration `display: block` and a declaration with property `vertical-align`. The following snippet is considered a violation: 
 ```
 .mybox {
    display: block;
    vertical-align: text-top;
}
 ```
**Actions**: Recognize rulesets, declarations with specific properties and values; find rulesets containing a declaration with property display and value block; check if they contain a declaration with property vertical-align.     
 
---
**Description**: Require properties appropriate for display (rule 4).   
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Require-properties-appropriate-for-display)  
**Violations**: A warning is issued when a ruleset contains a declaration with property display and value in the form table-\* and also contains a declaration with property margin, margin-top, margin-right, margin-bottom or margin-left. The following snippet is considered a violation: 
 ```
 .mybox {
    display: table-cell;
    margin: 10px;
}
 ```
**Actions**: Recognize rulesets, declarations with specific properties and value in a given form; find rulesets containing a declaration with property display and value that matches the form table-\*; check if it contains a declaration with any of the properties in the list [margin, margin-top, margin-right, margin-bottom, margin-left].     

---
**Description**: Disallow duplicate properties (rule 1).  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-duplicate-properties)  
**Violations**: A warning is issued when a ruleset contains a given declaration twice, i.e. when the property and the value are identical. The following snippet is considered a violation: 
 ```
 .mybox {
    border: 1px solid black;
    border: 1px solid black;
}
 ```
**Actions**: Compare couples of declarations within a rule; check if the two declarations have equal properties and values.     

---
**Description**: Disallow duplicate properties (rule 2).  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-duplicate-properties)  
**Violations**: A warning is issued when a ruleset contains a property twice and the two instances are separated by at least one other property. The following snippet is considered a violation: 
 ```
 .mybox {
    border: 1px solid black;
    color: green;
    border: 1px solid red;
}
 ```
**Actions**: Compare triples of declarations within a rule; check if the first and third have the same property and if the first and the second have different properties.     

---
**Description**: Disallow empty rules.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-empty-rules)  
**Violations**: Presence of rulesets that do not contain declarations. Sample violations are:
 ```
.myclass { }
.myclass { /* Comment */ }
```
In case at least one declaration is present, the ruleset does not violate the convention. The following snippet is not a violation:
```
.myclass { color: green; }
```
**Actions**: Recognize rulesets and declarations; determine whether a ruleset contains a declaration. 

---
**Description**: Disallow adjoining classes.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
**Violations**: Presence of class selectors immediately next to each other. Sample violations are:
 ```
.foo.bar {
    border: 1px solid black;
}
.first .abc.def {
    color: red;
}
```
Note that the rule does not refer to class selectors connected using the descendant selector:
```
.foo .bar {
    border: 1px solid black;
}
```
**Actions**: Find two classes that are immediate next to each other.

---
**Description**: Disallow the box-sizing property.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
**Violations**: Usage of box-sizing property. Sample violations are:
 ```
.mybox {
    box-sizing: border-box;
}
```
**Actions**: Find box-sizing property
 
---
**Description**: Require compatible vendor prefixes.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Drupal](https://www.drupal.org/node/1887862), [Moodle](https://docs.moodle.org/dev/CSS_coding_style)  
**Violations**: A warning is issues when a vendor-prefixed property is missing. For example, the following ruleset is missing transform properties with -moz, -o and -ms prefixes:
 ```
.mybox {
    -webkit-transform: translate(50px, 100px);
}
```
**Actions**: Find vendor-specific properties; check whether the rule that holds them also contains all other vendor-prefixed properties.
  


---
**Description**: Disallow negative indent.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
**Violations**: A warning is issued when a text-indent value of -99 or similar (i.e., -100, -999, etc.) is used without the use of direction: ltr. Sample violations are:
 ```
/* missing direction */
.mybox {
    text-indent: -999px;
}

/* missing direction */
.mybox {
    text-indent: -999em;
}

/* direction is rtl */
.mybox {
    direction: rtl;
    text-indent: -999em;
}
```

**Actions**: Find declarations with property text-indent and negative value; check whether the rule that holds them also contains a declaration of direction with value ltr.  

---
**Description**: Require standard property with vendor prefix.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules), [Moodle](https://docs.moodle.org/dev/CSS_coding_style)  
**Violations**: A warning is issued when a vendor-prefixed property is used without a standard property after it. Sample violations are:
 ```
/* missing standard property */
.mybox {
    -moz-border-radius: 5px;
}
```
Note that there might be more than one vendor prefixes. In such cases the standard property should appear after the last vendor-prefixed property.  
**Actions**: Find vendor-prefixed properties; check whether the following declaration does not exist; check whether the following declaration is not of the same property group.  
 
---
**Description**: Require a fallback color.
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules), [Moodle](https://docs.moodle.org/dev/CSS_coding_style)  
**Violations**: A warning is issued when a color property with a rgba(), hsl(), or hsla() color is used without a preceding color property that has an older color format, i.e. hexadecimal, named, or rgb(). Sample violations are:
 ```
.mybox {
    color: rgba(100, 200, 100, 0.5);
}
```
**Actions**: Find declarations with color property and rgba, hsl or hsla value; check if a previous declaration exists; check if the previous declaration has property color and value of type hex, color-name, rgb.  
 
---
**Description**: Disallow the star hack.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
**Violations**: A warning is issued when a property is preceded by an asterisk.
 ```
.mybox {
    border: 1px solid black;
    *width: 100px;
}
```
**Actions**: Find properties that start with an asterisk. 
 
---
**Description**: Disallow the underscore hack.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
**Violations**: A warning is issued when a property is preceded by an underscore.
 ```
.mybox {
    border: 1px solid black;
    _width: 100px;
}
```
**Actions**: Find properties that start with an underscore. 
 
---
**Description**: Bulletproof font face.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules), [Isobar](http://isobar-idev.github.io/code-standards/)  
**Violations**: A warning is issued if the first URL declaration does not contain the suffix '?#iefix'.
 ```
@font-face {
    font-family: 'MyFontFamily';
    src: url('myfont-webfont.eot') format('embedded-opentype')
}
```
The implementation provided by CSS lint does not have much in common with the description. Testing shows that instead of ensuring that the first url has the required suffix, CSS lint checks if the font-face rule contains a url with the required suffix. In fact, the following CSS code avoids the mentioned bug, but does not comply with the definition of the rule.
```
@font-face {
  font-family: 'MyWebFont';
  src: url('webfont.eot'); /* IE9 Compat Modes */
  src: url('webfont.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
       url('webfont.woff2') format('woff2'), /* Super Modern Browsers */
}
```
In conclusion, a violation occurs when a font-face rule does not contain a url with the suffix '?#iefix'.  
**Actions**: Find font-face statements; check they contain a url with the required suffix.  
  
---
**Description**: Do not use too many web fonts.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
**Violations**: A warning is issued when a stylesheet contains more than five @font-face declarations.  
**Actions**: Recognize @font-face declarations; count the occurrences of @font-face declarations; compare the number to a predefined value.  
 
---
**Description**: Disallow selectors that look like regular expressions.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules), [CodeGuide](http://codeguide.co/)  
**Violations**: Usage of any of the following attribute selectors: contains, starts with, ends with, word match, contains with dashes. Violations are:
 ```
 .mybox[class~=xxx]{
    color: red;
}
.mybox[class^=xxx]{
    color: red;
}
.mybox[class|=xxx]{
    color: red;
}
.mybox[class$=xxx]{
    color: red;
}
.mybox[class*=xxx]{
    color: red;
}
 ```
 The following two examples are not violations:
 ```
 .mybox[class=xxx]{
    color: red;
}
.mybox[class]{
    color: red;
}
 ```
**Actions**: Find any of the following selectors: *=, |=, ^=, $=, ~=  
 
---
**Description**: Disallow the universal selector.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules), [Isobar](http://isobar-idev.github.io/code-standards/)  
**Violations**: A warning is raised when the universal selector appears as the key simple-selector of a selector:
 ```
 * {
    color: red;
}
.selected * {
    color: red;
}
 ```
 However, if the selector is not key, there is no violation:
 ```
 .selected * a {
    color: red;
}
 ```
**Actions**: Find universal selector that is also the key simple-selector of a selector.  
 
---
**Description**: Disallow unqualified attribute selectors.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
**Violations**: The presence of an attribute selector as a key selector is considered a violation:
 ```
.selected [type=text] {
    color: red;
}
.myclass[type=text] {
    color: red;
}
 ```
 However, if the selector is not key, there is no violation:
 ```
.selected [type=text] a {
    color: red;
}
 ```
**Actions**: Find attribute selector that is also the key simple-selector of a selector.  
 
---
**Description**: Disallow overqualified elements.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules), [Isobar](http://isobar-idev.github.io/code-standards/), [Orion](http://wiki.eclipse.org/Orion/Coding_conventions#CSS), [CodeGuide](http://codeguide.co/), [CKAN](http://docs.ckan.org/en/latest/contributing/css.html)  
**Violations**: A violation occurs when an HTML tag and class name are used together. However, the cases when two different elements are found with the same class name are not considered violations.
 ```
/* violation */
li.active { ... }

/* OK */
li.active { ... }
p.active { ... }
 ```
**Actions**: Find HTML tags used in conjunction with classes. Count the number of unique tags that qualify each class. Check if the number is equal to 1.
 
---
**Description**: Avoid qualifying ID and class names with type selectors.  
**Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#Protocol), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Moodle](https://docs.moodle.org/dev/CSS_coding_style)  
**Violations**:  Do not use element names in conjunction with IDs or classes. Sample violations include:
 ```
ul#example {}
div.error {}
 ```
 The following snippets are not considered violations:
 ```
 #example {}
.error {}
 ```
**Actions**: Find HTML tags used in conjunction with classes or ids.
 
---
**Description**: Disallow duplicate background images.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
**Violations**:  The rule forbids the same url for background image to be included twice in the stylesheet. Sample violations include:
 ```
.heart-icon {
    background: url(sprite.png) -16px 0 no-repeat;
}
.task-icon {
    background: url(sprite.png) -32px 0 no-repeat;
}
 ```
**Actions**: Check whether the url values in background declarations are unique.
 
---
**Description**: Disallow too many floats.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
**Violations**:  Violations of this convention occur when a stylesheet contains more than 10 declarations of the float property.  
**Actions**: Count the number of occurrences of float; compare the number to 10.
 
---
**Description**: Do not use too many font size declarations.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
**Violations**:  Violations of this convention occur when a stylesheet contains more than 10 declarations of font-size.
 Note that the implementation provided by CSS lint takes into consideration only font-size declarations. Font declarations are disregarded.  
**Actions**: Count the number of occurrences of font-size; compare the number to 10.
 
---
**Description**: Disallow outline:none (rule 1).  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
**Violations**:  Violations of this convention occur when a rule contains declaration outline: none or outline: 0 and the selectors of the rule do not contain :focus.
 ```
a {
    outline: none;
}
a {
    outline: 0;
}
 ```
 Note that the implementation provided by CSS lint takes into consideration the presence of the :focus pseudo selector anywhere in the selector. Thus, a rule `a:focus p` does not yield a warning. Also, CSS lint does not check multiselectors. The rule `a:focus, p` is considered OK, which is obviously wrong.  
**Actions**: Find rulesets that contain declaration with specific property and value; check if the selector of the ruleset contains the :focus pseudo selector.
 
---
**Description**: Disallow outline:none (rule 2).  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
**Violations**:  Violations of this convention occur when a rule contains declaration outline: none or outline: 0 and a :focus pseudo selector, but does not contain any other declarations.
 ```
a:focus {
    outline: 0;
}
 ```
**Actions**: Find rulesets that contain declaration with specific property and value and the :focus pseudo selector; check they contain more than one declaration.
 
---
**Description**: Disallow qualified headings.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
**Violations**:  Violations of this convention occur when a ruleset contains a selector where the heading element is key and the selector contains more simple-selectors. Sample violations:
 ```
.box h3 {
    font-weight: normal;
}
.item:hover h3 {
    font-weight: bold;
}
 ```
 The following example is not a violation:
```
h3 {
    font-weight: normal;
}
```
**Actions**: Find selectors that have heading tags as key selectors; check whether the selectors contain other simple selectors
 
---
**Description**: Headings should only be defined once.  
**Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
**Violations**:  Violations of this convention occur when more than one ruleset defines properties targeted at the same heading.
 ```
h3 {
    font-weight: normal;
}
.box h3 {
    font-weight: bold;
}
 ```
 The following example is not a violation:
```
h3 {
    font-weight: normal;
}
h3:hover {
    font-weight: bold;
}
```
Note that CSS lint simply disregards the headings with pseudo selectors. Repeating the h3:hover selector in multiple rules does not yield a warning.  
**Actions**: Find key selectors that contain headings and do not contain pseudo selectors; check if two key-selectors contain the same heading.
 
---
**Description**: Require a fallback property for background-image declarations that use gradients.  
**Source**: [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important)  
**Violations**:  A violation occurs when a declaration of background-image uses a gradient value does not have a fallback declaration of background-color.
 ```
background-image: linear-gradient(top, #444444, #999999)
 ```
 The following example is not a violation:
```
background-color: #444444;
background-image: -webkit-linear-gradient(top, #444444, #999999);
```
**Actions**: Find declarations with property background-image and gradient value; check if a previous declaration exists; check if the previous declaration has a background-color property.  
 
---
**Description**: Strings should use double quotes.  
**Source**: [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Drupal](https://www.drupal.org/node/1887862), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [BackdropCMS](https://api.backdropcms.org/css-standards), [CKAN](http://docs.ckan.org/en/latest/contributing/css.html)  
**Violations**:  Violations of this convention occur when a string uses single quotes:
 ```
 font-family: "Arial Black"
 ```
**Actions**: Find strings; check if they use single quotes
 
---
**Description**: Use single quotation marks for attribute selectors.  
**Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Drupal](https://www.drupal.org/node/1887862), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [ss64](http://ss64.com/css/syntax-naming.html), [CodeGuide](http://codeguide.co/), [BackdropCMS](https://api.backdropcms.org/css-standards)  
**Violations**:  The convention refers to the values of attribute selectors. According to the [CSS specification](http://www.w3.org/TR/css3-selectors/#attribute-selectors), the values of attribute selectors can be CSS identifiers or strings. This the possible violations of this convention include 1) using double quotes or 2) not using quotes at all:
 ```
 span[class=example]
 span[class="example"]
 ```
**Actions**: Find attribute values; check if their type is string; check if they use double quotes
 
---
**Description**: Use double quotation marks in charsets.  
**Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes)  
**Violations**:  Using single quotes in charset is illegal according to CSS rules. Since the convention describes an anti-pattern, its violations occur when single quotes are used in a charset:
 ```
 @charset 'UTF-8';
 ```
**Actions**: Find strings in charsets; check if they use single quotes
 
---
**Description**: Do not use pt or rem.   
**Source**: [Moodle](https://docs.moodle.org/dev/CSS_coding_style)  
**Violations**: Usage of unit with value pt or rem. For example, the snippet `font-size: 12pt;` is a violation. The snippet `font-size: 1em;` does not violate the convention.  
**Actions**: Recognize units with value pt or rem  

---
**Description**: Use single quotes in values.  
**Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS)  
**Violations**:  Violations occur when values contain strings that use double quotes:
 ```
 font-family: "Verdana";
 ```
**Actions**: Find strings in values; check if they use double quotes.
 
---
**Description**: Font names with spaces must be surrounded by double quotes.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)  
**Violations**:  Font names appear in font or font-family declarations. Thus, a violation of this convention is a single-quote string that appears as a value of either of the declarations:
 ```
 font-family: 'Arial Black';
 ```
**Actions**: Find strings in values of declarations with properties 'font-family' or 'font'; check if they use single quotes.

---
**Description**: Do not use over-qualified selectors.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/)  
**Violations**:  Violations occur when an HTML tag appears immediately before a class or an id:
 ```
 div.container
 ```
**Actions**: Find HTML tags used in conjunction with a class or an id.
 
---
**Description**: Do not qualify ID rules with tag names or classes.  
**Source**: [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS)  
**Violations**:  The convention states that if a rule has an ID selector as its key selector, tags should not be added to the rule. Violations include:
 ```
button#backButton {…}
.menu-left#newMenuIcon {…}
 ```
**Actions**: Find an id that is also a key selector; check if the previous sibling is an HTML tag.
 
---
**Description**: Do not qualify class rules with tag names or classes.  
**Source**: [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS)  
**Violations**:  The convention states that if a rule has a class selector as its key selector, tags should not be added to the rule. Violations include:
 ```
treecell.indented {…}
 ```
**Actions**: Find a class that is also a key selector; check if the previous sibling is an HTML tag.
 
---
**Description**: Use the most specific category possible.  
**Source**: [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS), [CodeGuide](http://codeguide.co/)  
**Violations**:  The convention states that the single biggest cause of slowdown is too many rules in the tag category. Thus, instead of using tags as key selectors, we should use classes or ids. Violations include:
 ```
treeitem[mailfolder="true"] > treerow > treecell {…}
 ```
**Actions**: Find HTML tags that are also key selectors.
 
---
**Description**: Avoid the descendant selector.  
**Source**: [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/)  
**Violations**:  Violations of this guideline are the usages of the descendant selector:
 ```
treehead treerow treecell {...}
 ```
**Actions**: Find descendant selector.
 
---
**Description**: Avoid using the child selector with tag category rules.  
**Source**: [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS)  
**Violations**:  Violations of this convention are the selectors that have HTML tags as key selectors and contain a child selector:
 ```
treehead > treerow > treecell {...}
 ```
**Actions**: Find selectors that have HTML tags as their key selectors; check whether these selectors contain a child selector.
 
---
**Description**: Question all usages of the child selector.  
**Source**: [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/)  
**Violations**:  A warning should be raised when the child selector is used:
 ```
treeitem[IsImapServer="true"] > treerow > .tree-folderpane-icon {…}
 ```
**Actions**: Find child selectors.
 
---
**Description**: Avoid vendor-specific features unless necessary.  
**Source**: [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS)  
**Violations**:  A warning should be issued when a vendor-specific property is found:
 ```
-webkit-border-radius
-moz-border-radius
 ```
**Actions**: Find properties that are vendor-prefixed.  
 
---
**Description**: Put a semicolon at the end of each declaration  
**Source**: [phpied](http://www.phpied.com/css-coding-conventions/), [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Drupal](https://www.drupal.org/node/1887862), [CSSguidelines](http://cssguidelin.es/#introduction), [ss64](http://ss64.com/css/syntax-naming.html), [cbracco](https://github.com/cbracco/css-conventions), [Morshed](http://www.morshed-alam.com/2010/01/css-coding-guidelinesconventions.html), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [CodeGuide](http://codeguide.co/), [Toll](http://www.benjamintoll.com/software/css_code_conventions.html), [Moodle](https://docs.moodle.org/dev/CSS_coding_style), [BackdropCMS](https://api.backdropcms.org/css-standards), [Shayhowe](http://learn.shayhowe.com/html-css/writing-your-best-code/)  
**Violations**:  CSS allows the delimiter after the last declaration of a rule to be omitted. Since this can cause maintainability issues, the convention requires the delimiter after the last declaration to be present. Violations occur when the last declaration of a rule does not have a following delimiter.
 ```
.myclass{
  color: red;
  font-family: "Arial Black"
}
 ```
**Actions**: Find the last declaration of a ruleset; check if there is a declaration delimiter after it.
 
---
**Description**: Do not use shorthand properties, except border.  
**Source**: [phpied](http://www.phpied.com/css-coding-conventions/), [LiquidContract](http://wiki.liquid-contact.com/index.php?title=CSS_Coding_Conventions#Introduction), [CodeGuide](http://codeguide.co/)  
**Violations**:  A warning should be issued when any of the properties are encountered: margin, padding, background, font, list-style, transition  
**Actions**: Find properties that match the list [margin, padding, background, font, list-style, transition]  
 
---
**Description**: Do not put quotes in uri values.  
**Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Drupal](https://www.drupal.org/node/1887862), [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important), [CKAN](http://docs.ckan.org/en/latest/contributing/css.html)   
**Violations**:  A warning should be issued when the value of a url is of type string:
 ```
 url("//www.google.com/css/maia.css")
 ```
**Actions**: Find url values; check if their type is string.
 
---
**Description**: Use hex or rgba() for colors.  
**Source**: [GitHub](http://primercss.io/guidelines/#css), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/)  
**Violations**:  Violations include usages of color-names, rgb(), hsl() and hsla():
 ```
 color: red;
 color: rgb(50, 100, 150)
 ```
**Actions**: Find values that are color-names, rgb, hsl, or hsla.  
 
---
**Description**: Use rgba only when opacity is needed.   
**Source**: [GitHub](http://primercss.io/guidelines/#css), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/)  
**Violations**:  Violations are usages of rgba() with last argument equal to 1:
 ```
 background-color: rgba(255, 0, 0, 1);
 ```
**Actions**: Find rgba() values with opacity equal to 1.  
 
---
**Description**: Use short hexadecimal values.   
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Drupal](https://www.drupal.org/node/1887862), [Shayhowe](http://learn.shayhowe.com/html-css/writing-your-best-code/), [CKAN](http://docs.ckan.org/en/latest/contributing/css.html)  
**Violations**:  Presence of a hex value that is long and could be shortened. Long hex values contain 6 hexadecimal characters and short - 3 characters. Long hex values that could be shortened match the format #rrggbb. Sample violations:
```
#99EE11;
#ffffff;
```
The next examples do not violate the convention:
```#9E1;
#fff;
#E9E9E9
```
**Actions**: Find hex values that match the format #rrggbb.  
 
---
**Description**: Use the shorthand margin property.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules), [Moodle](https://docs.moodle.org/dev/CSS_coding_style), [Shayhowe](http://learn.shayhowe.com/html-css/writing-your-best-code/), [CKAN](http://docs.ckan.org/en/latest/contributing/css.html)  
**Violations**:  Violation of this convention is a rule that contains all four properties: margin-top, margin-right, margin-bottom, margin-left.
```
a {
  margin-top: 10px;
  margin-right: 15px;
  margin-bottom: 25px;
  margin-left: 15px;
}
```  

**Actions**: Find rulesets that contain all four properties in the list [margin-top, margin-right, margin-bottom, margin-left].  
 
---
**Description**: Use the shorthand padding property.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules), [Moodle](https://docs.moodle.org/dev/CSS_coding_style), [Shayhowe](http://learn.shayhowe.com/html-css/writing-your-best-code/), [CKAN](http://docs.ckan.org/en/latest/contributing/css.html)  
**Violations**:  Violation of this convention is a rule that contains all four properties: padding-top, padding-right, padding-bottom, padding-left.
```
a {
  padding-top: 10px;
  padding-right: 15px;
  padding-bottom: 25px;
  padding-left: 15px;
}
```  
**Actions**: Find rulesets that contain all four properties in the list [padding-top, padding-right, padding-bottom, padding-left]  


---
**Description**: Use the shorthand border property.   
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Moodle](https://docs.moodle.org/dev/CSS_coding_style), [Shayhowe](http://learn.shayhowe.com/html-css/writing-your-best-code/), [CKAN](http://docs.ckan.org/en/latest/contributing/css.html)  
**Violations**:  Violation of this convention is a rule that contains any of the properties: border-top, border-right, border-bottom, border-left, border-color, border-style.
```
.box {
  border-top: 1px;
}
```
**Actions**: Find rulesets that contain any of the properties in the list [border-top, border-right, border-bottom, border-left, border-color, border-style]. 
 
---
**Description**: Use the shorthand font property.   
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Moodle](https://docs.moodle.org/dev/CSS_coding_style), [Shayhowe](http://learn.shayhowe.com/html-css/writing-your-best-code/), [CKAN](http://docs.ckan.org/en/latest/contributing/css.html)  
**Violations**:  Violation of this convention is a rule that contains the two properties: font-size and font-family.
```
.box {
  font-size: 18em;
  font-family: Fantasy;
}
```
**Actions**: Find rulesets that contain the font-size and font-family properties.  
 
---
**Description**: Use the shorthand list-style property.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Moodle](https://docs.moodle.org/dev/CSS_coding_style), [Shayhowe](http://learn.shayhowe.com/html-css/writing-your-best-code/), [CKAN](http://docs.ckan.org/en/latest/contributing/css.html)  
**Violations**:  Violation of this convention is a rule that contains any of the three properties: list-style-type, list-style-position, list-style-image.
```
ul {
 list-style-type: square;
}
```
**Actions**: Find rulesets that contain any of the properties in the list [list-style-type, list-style-position, list-style-image]

---
**Description**: Do not use units after zero values.   
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Drupal](https://www.drupal.org/node/1887862),[GitHub](http://primercss.io/guidelines/#css), [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [CodeGuide](http://codeguide.co/), [Moodle](https://docs.moodle.org/dev/CSS_coding_style), [BackdropCMS](https://api.backdropcms.org/css-standards), [Shayhowe](http://learn.shayhowe.com/html-css/writing-your-best-code/)   
**Violations**:  Violation occur when dimensions or percentages have 0 values:
```
.box { margin-top: 0px; }
.mybox { margin-bottom: 0%; }
```
**Actions**: Find dimensions and percentages that have 0 value.
 
---
**Description**: Use px for font-size.   
**Source**: [GitHub](http://primercss.io/guidelines/#css), [Isobar](http://isobar-idev.github.io/code-standards/)  
**Violations**: Violations are font-size declarations that use units different than px: em, rem, cm etc.
```
font-size: 1.5em;
```
**Actions**: Find font-size declarations that contain dimensions with units different than px.
 
---
**Description**: Line height should be unit-less.   
**Source**: [GitHub](http://primercss.io/guidelines/#css), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Isobar](http://isobar-idev.github.io/code-standards/)  
**Violations**: Violations are line-height that contain units.  
**Actions**: Find line-height declarations that contain units.

---
**Description**: Use a leading zero for decimal values.   
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [CodeGuide](http://codeguide.co/)  
**Violations**:  Violation occurs when a number with value in the interval (-1,1) does not start with a 0 character:
```
.box { font-size: .8em; }
```
**Actions**: Find decimal values that start with '.' or '-.'

---
**Description**: All values in media queries have to be written in rems, unless it is inappropriate.   
**Source**: [Drupal](https://www.drupal.org/node/1887862)  
**Violations**: Violations occur when media queries use dimensions with units other than rem:
```
@media screen and (min-width: 450px) { ... }
```
**Actions**: Find dimensions in media queries; check whether their units are rem

---
**Description**: Avoid presentation-specific words in selector names.   
**Source**: [phpied](http://www.phpied.com/css-coding-conventions/), [ss64](http://ss64.com/css/syntax-naming.html), [Morshed](http://www.morshed-alam.com/2010/01/css-coding-guidelinesconventions.html), [Isobar](http://isobar-idev.github.io/code-standards/), [Apppie](http://www.apppie.org/pages/approach/naming.html)  
**Violations**: Violations occur when a word in an id or a class has presentation meaning. Although such violations are very hard to detect, one approach is to check whether the word is a color or belongs to a predefined list of forbidden words.
```
.blue { ... }
#text-gray { ... }
.light-box { ... }
```
**Actions**: Find words in id and class selectors; check if words are colors  
  
---
**Description**: Do not abbreviate.   
**Source**: [phpied](http://www.phpied.com/css-coding-conventions/), [Apppie](http://www.apppie.org/pages/approach/naming.html), [Moodle](https://docs.moodle.org/dev/CSS_coding_style), [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)  
**Violations**: Violations occur when a word in an id or a class is not present in the dictionary.
```
.prod { ... }
#txt { ... }
```
The following two examples are not considered violations:
```
.production { ... }
#text { ... }
```
**Actions**: Find words in id and class selectors; check if words are present in the dictionary  

---
**Description**: Id and class names should be lowercase and separated by dashes(or underscores).  
**Source**: [phpied](http://www.phpied.com/css-coding-conventions/),[Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important), [CSSguidelines](http://cssguidelin.es/#introduction), [LiquidContract](http://wiki.liquid-contact.com/index.php?title=CSS_Coding_Conventions#Introduction), [ss64](http://ss64.com/css/syntax-naming.html), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [CodeGuide](http://codeguide.co/), [Apppie](http://www.apppie.org/pages/approach/naming.html), [Moodle](https://docs.moodle.org/dev/CSS_coding_style), [CKAN](http://docs.ckan.org/en/latest/contributing/css.html)   
**Violations**: Violations occur when an id or a class contains a symbol other than dashes and lowercase letters.
```
.Prod { ... }
#text-case { ... }
```
**Actions**: Find id and class selectors; check if their names contain characters other than lowercase letters or dashes

---
**Description**: Require id and class names to be lowercase  
**Source**: [phpied](http://www.phpied.com/css-coding-conventions/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [cbracco](https://github.com/cbracco/css-conventions), [Morshed](http://www.morshed-alam.com/2010/01/css-coding-guidelinesconventions.html), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS)  
**Violations**: Violations occur when an id or a class contains an uppercase letter.
```
.Prod_rule { ... }
#textCase { ... }
```
**Actions**: Find id and class selectors; check if their names contain uppercase letters

---
**Description**: Id and class names should use camelCase.  
**Source**: [Realdeal](http://www.realdealmarketing.net/docs/css-coding-style.php), [Isobar](http://isobar-idev.github.io/code-standards/), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS)  
**Violations**: Violations occur when an id or class name does not match the pattern `[a-z][A-Za-z]*`.
```
.production_Rule { ... }
#TextRule { ... }
```
**Actions**: Find id and class selectors; check if their names match a given pattern

---
**Description**: Avoid using attributes in selector names.  
**Source**: [Realdeal](http://www.realdealmarketing.net/docs/css-coding-style.php)  
**Violations**: Violations occur when an id or class name contains a word that is a value in the rule.
```
.red { color: red; }
```
**Actions**: Find id and class words; check if words match any of the values contained in its ruleset

---
**Description**: Do not use specific words in id and class names.  
**Source**: [Realdeal](http://www.realdealmarketing.net/docs/css-coding-style.php)  
**Violations**: Violations occur when a word of an id or class matches any of the values of a predefined list. Particularly, the convention refers to the words html, head, bottom, top, left and right.
```
.box-top { color: red; }
```
**Actions**: Find id and class words; check if words match any of the values specified in a list

---
**Description**: Properties should be lowercase, except for vendor-specific ones.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Moodle](https://docs.moodle.org/dev/CSS_coding_style)  
**Violations**: Violations occur when a non vendor-prefixed property uses uppercase letters:
```
Color: red;
MARGIN: 10px;
```
The following examples are not considered violations:
```
color: red;
-MOZ-border-radius: 5px;
```
**Actions**: Find non vendor-prefixed properties; check if they contain any uppercase letters

---
**Description**: HTML elements should be lowercase.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [cbracco](https://github.com/cbracco/css-conventions), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [Moodle](https://docs.moodle.org/dev/CSS_coding_style)  
**Violations**: Violations occur when an HTML tag contains uppercase letters:
```
H1 { ... };
```
**Actions**: Find HTML tags; check if they contain any uppercase letters

---
**Description**: Attributes should be lowercase.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [cbracco](https://github.com/cbracco/css-conventions)  
**Violations**: Violations occur when an attribute contains uppercase letters:
```
[PROP] { ... };
```
**Actions**: Find attribute selectors; check if they contain any uppercase letters

---
**Description**: Attributes values should be lowercase.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [cbracco](https://github.com/cbracco/css-conventions)  
**Violations**: Violations occur when an attribute value contains uppercase letters:
```
[property='VALUE'] { ... };
```
**Actions**: Find attribute values; check if they contain any uppercase letters

---
**Description**: Values should be lowercase, except for strings.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [cbracco](https://github.com/cbracco/css-conventions)  
**Violations**: Violations occur when a property value other than a string contains uppercase letters:
```
color: RED;
margin-top: 3PX;
```
**Actions**: Find values different than strings; check if they contain any uppercase letters

---
**Description**: Never reference 'js-' prefixed class names from CSS files. 'js-' is used exclusively from JS files. Use the 'is-' prefix for state rules that are shared between CSS and JS.  
**Source**: [GitHub](http://primercss.io/guidelines/#css), [CodeGuide](http://codeguide.co/)  
**Violations**: Violations occur when a class name has a 'js-' prefix:
```
.js-box { ... }
```
**Actions**: Find classes; check if they have a 'js-' prefix

---
**Description**: Hexadecimal values should be lowercase.  
**Source**: [Drupal](https://www.drupal.org/node/1887862), [ss64](http://ss64.com/css/syntax-naming.html), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [CodeGuide](http://codeguide.co/), [Moodle](https://docs.moodle.org/dev/CSS_coding_style), [BackdropCMS](https://api.backdropcms.org/css-standards), [Shayhowe](http://learn.shayhowe.com/html-css/writing-your-best-code/)  
**Violations**: Violations occur when a hexadecimal value contains uppercase letters:
```
color: #FFF;
```
**Actions**: Find hexadecimal values; check if they contain uppercase letters

---
**Description**: Put a table of contents at the beginning of every file.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [CSSguidelines](http://cssguidelin.es/#introduction), [cbracco](https://github.com/cbracco/css-conventions), [CSS Wizardry](http://csswizardry.com/2012/04/my-html-css-coding-style/), [Mediarain](http://standards.mediarain.com/html-css)    
**Violations**: Violations occur when the stylesheet does not start with a comment.  
**Actions**: Check if the first element of the file is a comment

---
**Description**: Add the comment /\* LTR \*/ on the same line where you use the values 'left' or 'right'.  
**Source**: [Drupal](https://www.drupal.org/node/1887862)    
**Violations**: Violations occur when there is not a /\* LTR \*/ comment following a declaration with value 'left' or 'right'.  
**Actions**: Find declarations where the value is 'left' or 'right'; check if there is a comment of the form ' LTR ' following the declaration

---
**Description**: Add the comment /\* LTR \*/ on the same line where you specify the direction of the language to ltr.  
**Source**: [Drupal](https://www.drupal.org/node/1887862)    
**Violations**: Violations occur when there is not a /\* LTR \*/ comment following a declaration with property direction and value ltr.  
**Actions**: Find declarations with property direction and value ltr; check if there is a comment of the form ' LTR ' following the declaration

---
**Description**: Use 4 (or 2) spaces for indentation.  
**Source**: [phpied](http://www.phpied.com/css-coding-conventions/), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Drupal](https://www.drupal.org/node/1887862), [GitHub](http://primercss.io/guidelines/#css), [LiquidContract](http://wiki.liquid-contact.com/index.php?title=CSS_Coding_Conventions#Introduction), [ss64](http://ss64.com/css/syntax-naming.html), [cbracco](https://github.com/cbracco/css-conventions), [Isobar](http://isobar-idev.github.io/code-standards/), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [CodeGuide](http://codeguide.co/), [Mediarain](http://standards.mediarain.com/html-css), [Toll](http://www.benjamintoll.com/software/css_code_conventions.html), [Moodle](https://docs.moodle.org/dev/CSS_coding_style), [CKAN](http://docs.ckan.org/en/latest/contributing/css.html)    
**Violations**: Violations occur when line indentation contains other than spaces or the number of spaces is not a multiple of 4.  
**Actions**: Find indentation of a line; check if it contains only spaces; check if the number of spaces is a multiple of the specific value

---
**Description**: Indent declarations once.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important),  [Drupal](https://www.drupal.org/node/1887862), [CSSguidelines](http://cssguidelin.es/#introduction), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [BackdropCMS](https://api.backdropcms.org/css-standards)    
**Violations**: Violations occur when a declaration is not indented exactly once compared to its ruleset. Note that a ruleset might be nested inside a media at-rule and in such cases declarations need to be indented twice. Thus, the rule specifies the require indentation only compared to the rule that contains the declaration.  
**Actions**: Find declarations; check if they are indented one level compared to the rule that contains them

---
**Description**: Indent the contents of a block.  
**Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes)    
**Violations**: Note that this rule differs from the previous one. Instead of targeting declarations, this convention refers to all elements of a declaration block that appear after a newline. While the following snippet is valid according to the previous rule, it is a violation of the current convention:
 ```
 selector {
 /* comment that is not indented */
     property: value;
 }
 ```
**Actions**: Find all elements of a block that appear after a newline; check if they are indented one level compared to the start of the block

---
**Description**: Closing curly bracket of a block has to be indented with the selector of the rule.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important), [Drupal](https://www.drupal.org/node/1887862), [LiquidContract](http://wiki.liquid-contact.com/index.php?title=CSS_Coding_Conventions#Introduction), [ss64](http://ss64.com/css/syntax-naming.html), [cbracco](https://github.com/cbracco/css-conventions), [Mediarain](http://standards.mediarain.com/html-css), [Moodle](https://docs.moodle.org/dev/CSS_coding_style)    
**Violations**: Violations occur when the closing bracket is not vertically indented with the beginning of the first selector of the corresponding rule
 ```
 selector {
     property: value;
     }
 ```
**Actions**: Find rulesets; check if their selector is vertically aligned with the closing bracket of the declaration block

---
**Description**: Align vertically vendor properties.  
**Source**: [CSSguidelines](http://cssguidelin.es/#introduction), [ss64](http://ss64.com/css/syntax-naming.html), [cbracco](https://github.com/cbracco/css-conventions), [Moodle](https://docs.moodle.org/dev/CSS_coding_style)    
**Violations**: Violations occur when vendor-prefixed properties are not right-aligned:
 ```
.foo {
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 3px;
}
 ```
**Actions**: Find consecutive declarations that belong to the same standard property group; check if the declarations are aligned to the right

---
**Description**: Align vertically the values of adjacent properties that belong to the same logical group: top bottom left right, margin\*, padding\*.  
**Source**: [CSSguidelines](http://cssguidelin.es/#introduction)  
**Violations**: Violations occur when values of related properties are not vertically aligned to the left:
```
.bar { 
    margin-right: -10px;
    margin-left: -10px;
    padding-right: 10px;
    padding-left:  10px;
}
```
This is the correct alignment:
```
.bar { 
    margin-right: -10px;
    margin-left:  -10px;
    padding-right: 10px;
    padding-left:  10px;
}
```
**Actions**: Find related properties; check if their values are vertically aligned

---
**Description**: Align vertically vendor-specific values.  
**Source**: [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important)  
**Violations**: Violations occur when vendor specific values are not aligned vertically to the right:
```
.foo {
	background-image: linear-gradient(top, #444444, #999999);
	background-image: -o-linear-gradient(top, #444444, #999999);
	background-image: -moz-linear-gradient(top, #444444, #999999);
	background-image: -webkit-linear-gradient(top, #444444, #999999);
	background-image: -webkit-gradient(linear, left top, left bottom, from(#444444), to(#999999));
}
```
This is the correct alignment:
```
.foo {
	background-color: #444444;
	background-image: -webkit-gradient(linear, left top, left bottom, from(#444444), to(#999999));
	background-image: -webkit-linear-gradient(      top, #444444, #999999);
	background-image:    -moz-linear-gradient(      top, #444444, #999999);
	background-image:      -o-linear-gradient(      top, #444444, #999999);
	background-image:         linear-gradient(to bottom, #444444, #999999);
}
```
**Actions**: Find related vendor-speicifc values; check if they are vertically aligned
 
---
**Description**: Indent multiline selectors.  
**Source**: [Realdeal](http://www.realdealmarketing.net/docs/css-coding-style.php)   
**Violations**: Violations occur if the any of the selectors in a multiline selector, except the first, are not indented once, compared to the first selector:
```
.class1,
	class2,
	class3,
	class4 { font-size: 80%; }
.otherClass { font-size: 2em; }
```
**Actions**: Find all but the first selectors in a multiline selector; check if they are indented once compared to the first selector 

---
**Description**: Rulesets in media queries should be indented once.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Drupal](https://www.drupal.org/node/1887862), [BackdropCMS](https://api.backdropcms.org/css-standards)   
**Violations**: Violations occur when rulesets in media at-rules are not indented once:
```
@media all and (max-width: 699px) and (min-width: 520px) {
    .class { ... }
}
```
**Actions**: Find rulesets that are nested in media queries; check if they are indented once compared to the media at-rule

---
**Description**: Comments should be indented with the thing they describe.  
**Source**: [Drupal](https://www.drupal.org/node/1887862), [Moodle](https://docs.moodle.org/dev/CSS_coding_style), [BackdropCMS](https://api.backdropcms.org/css-standards)   
**Violations**: Violations occur when a comment is not indented with the declaration it describes:
```
/* a fix */
   color: red !important;
```
**Actions**: Find comments that appear before a declaration; check if they are vertically aligned with the declaration after them

---
**Description**: Add one blank line between rulesets.  
**Source**: [phpied](http://www.phpied.com/css-coding-conventions/), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [GitHub](http://primercss.io/guidelines/#css), [CSSguidelines](http://cssguidelin.es/#introduction), [cbracco](https://github.com/cbracco/css-conventions), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [Mediarain](http://standards.mediarain.com/html-css), [Moodle](https://docs.moodle.org/dev/CSS_coding_style)     
**Violations**: Violations occurs when there is not exactly one blank line between rulesets:
```
a { ... }
b { ... } /* no blank line */


c { ... } /* two blank lines instead of one */
```
**Actions**: Find two adjacent rulesets; check if there is not an empty line between them

---
**Description**: Single-line rules may appear on adjacent lines.  
**Source**: [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [CSSguidelines](http://cssguidelin.es/#introduction), [BackdropCMS](https://api.backdropcms.org/css-standards)     
**Violations**: Note that this convention relaxes the constraints of the previous convention. It states that in specific circumstances, there might not be a blank line, but a single newline character. Its violations are the cases in which single-line rules appear on the same line or have more than one blank line between them:
```
a { property: value; } b { property: value; } /* same line */


c { property: value; } /* two blank lines instead of one */
```
**Actions**: Find two adjacent rulesets that contain a single declaration; check if there is a one or two newline symbols between them. 

---
**Description**: Values should appear on one line.  
**Source**: [Idiomatic CSS](https://github.com/necolas/idiomatic-css)         
**Violations**: Violations occur when a value is spread on two or more lines:
```
margin: 0px
        20px
        0px
        10px;
```
**Actions**: Find values and check if they are positioned on one lines  

---
**Description**: No space before colons.  
**Source**: [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important), [Drupal](https://www.drupal.org/node/1887862), [CSS Wizardry](http://csswizardry.com/2012/04/my-html-css-coding-style/), [Mediarain](http://standards.mediarain.com/html-css), [Toll](http://www.benjamintoll.com/software/css_code_conventions.html), [BackdropCMS](https://api.backdropcms.org/css-standards)     
**Violations**: Violations occur when there is a space between the property and the colon of a declaration:
```
color : red;
```
**Actions**: Find properties; check if there is a space immediately after them 

---
**Description**: Put one space after colons.  
**Source**: [phpied](http://www.phpied.com/css-coding-conventions/), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Drupal](https://www.drupal.org/node/1887862), [GitHub](http://primercss.io/guidelines/#css), [CSSguidelines](http://cssguidelin.es/#introduction), [LiquidContract](http://wiki.liquid-contact.com/index.php?title=CSS_Coding_Conventions#Introduction), [Morshed](http://www.morshed-alam.com/2010/01/css-coding-guidelinesconventions.html), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [CodeGuide](http://codeguide.co/), [Mediarain](http://standards.mediarain.com/html-css), [Toll](http://www.benjamintoll.com/software/css_code_conventions.html), [Moodle](https://docs.moodle.org/dev/CSS_coding_style), [BackdropCMS](https://api.backdropcms.org/css-standards), [Shayhowe](http://learn.shayhowe.com/html-css/writing-your-best-code/), [CKAN](http://docs.ckan.org/en/latest/contributing/css.html)      
**Violations**: Violations occur when a there is not a space after the colon of a declaration:
```
color:red;
```
**Actions**: Find colons in declarations; check if there is not one space immediately after them

---
**Description**: Put no spaces after colons.  
**Source**: [CSS Wizardry](http://csswizardry.com/2012/04/my-html-css-coding-style/)     
**Violations**: Violations occur when a there is a space after the colon of a declaration:
```
color: red;
```
**Actions**: Find colons in declarations; check if there is a space immediately after them

---
**Description**: Put one space between the last selector and the block.  
**Source**: [phpied](http://www.phpied.com/css-coding-conventions/), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Drupal](https://www.drupal.org/node/1887862), [GitHub](http://primercss.io/guidelines/#css), [CSSguidelines](http://cssguidelin.es/#introduction), [LiquidContract](http://wiki.liquid-contact.com/index.php?title=CSS_Coding_Conventions#Introduction), [ss64](http://ss64.com/css/syntax-naming.html), [cbracco](https://github.com/cbracco/css-conventions), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [CodeGuide](http://codeguide.co/), [Mediarain](http://standards.mediarain.com/html-css), [Shayhowe](http://learn.shayhowe.com/html-css/writing-your-best-code/), [CKAN](http://docs.ckan.org/en/latest/contributing/css.html)      
**Violations**: Violations occur when (1) there is not a space after the colon of a declaration or (2) there is more than one space after the colon:
```
a{ ... }
a   { ... }
```
**Actions**: Find selectors followed by declaration blocks; check if there is not exactly one space between them

---
**Description**: Opening brace must be on the same line as the last selector.  
**Source**: [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important), [LiquidContract](http://wiki.liquid-contact.com/index.php?title=CSS_Coding_Conventions#Introduction), [Morshed](http://www.morshed-alam.com/2010/01/css-coding-guidelinesconventions.html), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [Mediarain](http://standards.mediarain.com/html-css), [Toll](http://www.benjamintoll.com/software/css_code_conventions.html)      
**Violations**: This convention is slightly less restrictive than the previous one. While the former guideline requires exactly one space, the current convention disallows the usage of newlines:
```
a
{ ... }
```
**Actions**: Find selectors followed by declaration blocks; check if there is a newline between them

---
**Description**: Put the first declaration on a newline after the opening curly brace.  
**Source**: [CSSguidelines](http://cssguidelin.es/#introduction), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [Mediarain](http://standards.mediarain.com/html-css), [Toll](http://www.benjamintoll.com/software/css_code_conventions.html)       
**Violations**: Violations occur when the first declaration does not appear on the next line:
```
a { color: red; }

a { 

color: red; 

}
```
**Actions**: Find the opening brace of a declaration block and the first declaration of a block; check if the newline symbols between them are not equal to 1

---
**Description**: You may not use the "border" shorthand to set the border-color property.   
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when a color appears in the value of a border declaration.  
**Actions**: Find occurrences of border that contain colors.  

---
**Description**: You may not use the "background" shorthand to set the background-color property.   
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when a color appears in the value of a background declaration.  
**Actions**: Find occurrences of background that contain colors.  

---
**Description**: It is forbidden to use pt, use px instead.   
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when a value contains pt.  
**Actions**: Find occurrences of pt unit.  

---
**Description**: In multiselectors, order the selectors in by type: HTML, HTML groupings, classes, ids.   
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when the selectors are not ordered in the defined way.  
**Actions**: Find selectors in multiselectors. Assert the order of the selectors based on their type.  

---
**Description**: Paddings, dimensions & margins are ordered from the outer to the inner (padding, dimension, margin).   
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when a margin appears before padding or dimension and a dimension appears before padding.  
**Actions**: Find properties that match the specified groups. Assert their order is as specified.  

---
**Description**: Alignments and positioning are ordered from the outer to the inner (position, float, overflow, vertical-align, text-align, direction, text-indent, white-space).   
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when a margin when properties of the two groups are not ordered in the given way.  
**Actions**: Find properties that match the specified groups. Assert their order is as specified.  

---
**Description**: When setting border value, use always width followed by style.   
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when the value of the border property does not have style after the width value part.  
**Actions**: Find the width value part of the border declaration. Assert there is a style value part next to it.  

---
**Description**: Require newline before a declaration.   
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when a declaration does not have a newline before it.  
**Actions**: Find declarations and assert there is a newline before them.  

---
**Description**: It is always forbidden to have several properties set on a single line if a shorthand property is used.   
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when two declarations appear on the same line and at least one of them is a shorthand.  
**Actions**: Find declarations that appear on the same line and assert none of them is shorthand.  

---
**Description**: Require a header comment of the CSS file.    
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when the file does not start with a comment.  
**Actions**: Find the first node of the stylesheet and ensure it is a comment.  

---
**Description**: if you use comments put the after them after the ; at the end of the declaration.    
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when a comment does not appear at the end of a declaration line.   
**Actions**: Find comments and assert they appear at the end of the line before a declaration.  

---
**Description**: All except comments should be lowercase.    
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when any string that is not of type comment contains an uppercase letter.   
**Actions**: Find nodes that are not of type comment and assert that their string is lowercase.  

---
**Description**: Your ids and classes should not be more than 20 chars.    
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations id selectors are more than 20 chars.   
**Actions**: Find id selectors and assert their length is not more than 20 chars.  

---
**Description**: Do not use shorthands except when all sides are the same value.    
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when shorthand properties are used and they are given more than one value.   
**Actions**: Find shorthand declaration and assert the value is a single number.  

---
**Description**: Do not use shorthands except setting border width and style.    
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when shorthand properties are used, except for the border property.   
**Actions**: Find shorthand properties except for the border property.  

---
**Description**: Do not use shorthands except for setting background image.    
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when shorthand properties are used, except for the background property.   
**Actions**: Find shorthand properties except for the background property.  

---
**Description**: Do not use shorthands except list-type.    
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when shorthand properties are used, except for the list-style property.   
**Actions**: Find shorthand properties except for the list-style property.  

---
**Description**: Colors should be in hex, except for white, black and transparent, which should be in text.    
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when a color with value white, black or transparent is not expressed as color text and when any other color is not expressed in hex.   
**Actions**: Find hex colors and check whether they are white, black. Find color text colors and check whether they are different than while, black and transparent.  

---
**Description**: Forbid a class and a id to have the same value.    
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur when an id and a class share a name.     
**Actions**: Find all id names and check if the stylesheet contains a class of the same name.  

---
**Description**: The argument of a url must be in single quotes    
**Source**: [nodewave](http://ovh.nodewave.com/documents/coding-guidelines/css/export/css-coding-style-conventions--standards-guidelines-rules-v1.3.pdf)   
**Violations**: Violations occur the argument in a url uses double quotes or does not use quotes at all.     
**Actions**: Find the argument of urls and assert the type is string and that it contains single quotes.  

---
**Description**: One selector per line.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Drupal](https://www.drupal.org/node/1887862), [GitHub](http://primercss.io/guidelines/#css), [CSSguidelines](http://cssguidelin.es/#introduction), [cbracco](https://github.com/cbracco/css-conventions), [CodeGuide](http://codeguide.co/), [Mediarain](http://standards.mediarain.com/html-css), [Toll](http://www.benjamintoll.com/software/css_code_conventions.html), [Moodle](https://docs.moodle.org/dev/CSS_coding_style)         
**Violations**: Violations occur if adjacent selectors of a multiselector do not appear on adjacent lines:
```
h1, h2, h3 { ... }

h1,

h2 { ... }
```
**Actions**: Find adjacent selectors in a multiselector; check if there is one newline symbol between them

---
**Description**: Properties and values should be on the same line.  
**Source**: [CSSguidelines](http://cssguidelin.es/#introduction)         
**Violations**: Violations occur when a declaration spans over more than one line:
```
margin: 0px
        20px
        0px
        10px;
```
**Actions**: Find declarations; check if they contain the newline symbol

---
**Description**: Put every declaration on a new line  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Drupal](https://www.drupal.org/node/1887862), [GitHub](http://primercss.io/guidelines/#css), [CSSguidelines](http://cssguidelin.es/#introduction), [LiquidContract](http://wiki.liquid-contact.com/index.php?title=CSS_Coding_Conventions#Introduction), [ss64](http://ss64.com/css/syntax-naming.html), [cbracco](https://github.com/cbracco/css-conventions), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [CodeGuide](http://codeguide.co/), [Toll](http://www.benjamintoll.com/software/css_code_conventions.html), [Moodle](https://docs.moodle.org/dev/CSS_coding_style), [CKAN](http://docs.ckan.org/en/latest/contributing/css.html)         
**Violations**: Violations occur when declarations occur on the same line:
```
margin-left: 10px; margin-right: 10px;
```
**Actions**: Find adjacent declarations; check if there is not a newline symbol between them

---
**Description**: Place closing brace on a new line.  
**Source**: [Drupal](https://www.drupal.org/node/1887862), [GitHub](http://primercss.io/guidelines/#css), [CSSguidelines](http://cssguidelin.es/#introduction), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [CodeGuide](http://codeguide.co/), [Toll](http://www.benjamintoll.com/software/css_code_conventions.html)         
**Violations**: Violations occur when the closing brace of the declaration block appears on the same line:
```
a {
  property: value; }
```
**Actions**: Find closing brace of declaration blocks; check if there is not a newline symbol before it

---
**Description**: For short styles you can use one-liners.  
**Source**: [Realdeal](http://www.realdealmarketing.net/docs/css-coding-style.php), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [GitHub](http://primercss.io/guidelines/#css), [CSSguidelines](http://cssguidelin.es/#introduction), [cbracco](https://github.com/cbracco/css-conventions), [CodeGuide](http://codeguide.co/)         
**Violations**: This convention relaxes the constaints of a number of conventions. It states that if a ruleset contains a single declaration, it may appear in the form `selector { property: value; }`:
```
ul { margin: 10px 20px; }
```
**Actions**: Find rulesets with one declaration; check if they do not have a newline between the "{" and the declaration and between the declaration and the "}" or if they do not have a space between the "{" and the declaration and between the declaration and the "}"

---
**Description**: Do not put a space after the '(' of functions.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/),[Drupal](https://www.drupal.org/node/1887862), [BackdropCMS](https://api.backdropcms.org/css-standards)   
**Violations**: Violations occur when a space appears after the '(' symbol:
```
rgb( 100, 100, 100);
```
**Actions**: Find '(' symbol; check if there is a space after it

---
**Description**: Do not put a space before ')'  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/),[Drupal](https://www.drupal.org/node/1887862), [BackdropCMS](https://api.backdropcms.org/css-standards)   
**Violations**: Violations occur when a space appears before the ')' symbol:
```
rgb(100, 100, 100 );
```  
**Actions**: Find ')' symbol; check if there is a space before it

---
**Description**: Multiple csv values should be separated by a space  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/),[Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Drupal](https://www.drupal.org/node/1887862), [ss64](http://ss64.com/css/syntax-naming.html), [ThinkUp](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS), [CodeGuide](http://codeguide.co/), [BackdropCMS](https://api.backdropcms.org/css-standards)   
**Violations**: Violations occur when there is not a space after the csv delimiter:
```
rgb(100,100,100);
```
**Actions**: Find csv delimiters; check if there is not a after them

---
**Description**: Do not include spaces after commas within rgb(), rgba(), hsl(), hsla(), or rect() values.  
**Source**: [CodeGuide](http://codeguide.co/)  
**Violations**: Violations occur when there is a space after the delimiter in rgb, rgba, hsl, hsla, rect:
```
rgb(100, 100, 100);
hsla(100,  100,  100);
```
**Actions**: Find delimiters in functions rgb, rgba, hsl, hsla, rect; check if there is a after them

---
**Description**: Newlines should be used for lengthier multi-part values such as those for shorthand properties like box-shadow and text-shadow.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Drupal](https://www.drupal.org/node/1887862)   
**Violations**: Violations occur when the values that exceed a given length do not contain newlines.  
**Actions**: Find the values that span over more than 40 characters; check if they do not contain newline symbols

---
**Description**: Place comments on a new line.  
**Source**: [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [LiquidContract](http://wiki.liquid-contact.com/index.php?title=CSS_Coding_Conventions#Introduction)   
**Violations**: Violations occur when a comment does not have newline symbols before and after it.  
**Actions**: Find comments; check if they do not have newline symbols before and after them

---
**Description**: Group like properties together. The baseline for ordering is: Display, Positioning, Box model, Colors and Typography, Other.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Drupal](https://www.drupal.org/node/1887862), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide), [cbracco](https://github.com/cbracco/css-conventions), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [BackdropCMS](https://api.backdropcms.org/css-standards)   
**Violations**: Violations occur when two properties from different groups are not arranged accoring to the predefined order.  
**Actions**: Find every pair of properties within a ruleset; retrieve the group to which each property belongs; check if the properties do not conform to the specified order   

---
**Description**: Put declarations in alphabetical order. Ignore vendor specific prefixes for sorting.   
**Source**: [GitHub](http://primercss.io/guidelines/#css), [CSSguidelines](http://cssguidelin.es/#introduction), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide), [CodeGuide](http://codeguide.co/), [Mediarain](http://standards.mediarain.com/html-css), [Toll](http://www.benjamintoll.com/software/css_code_conventions.html)   
**Violations**: Violations occur when two adjacent properties are not in alphabetical order.  
**Actions**: Find every pair of adjacent properties within a ruleset; check if the appear in alphabetical order  

---
**Description**: Multiple vendor-prefixed properties should be alphabetically sorted.   
**Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide)   
**Violations**: Violations occur when two adjacent vendor-prefixed properties are not in alphabetical order.  
**Actions**: Find every pair of adjacent vendor-prefixed properties within a ruleset; check if the appear in alphabetical order  

---
**Description**: Use TRBL order for margin and padding.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Drupal](https://www.drupal.org/node/1887862), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [cbracco](https://github.com/cbracco/css-conventions)   
**Violations**: Violations occur when the properties are not arranged in the specified order.  
**Actions**: Find every pair of the margin\* or padding\* properties within a ruleset; check if the properties do not conform to the specified order   

---
**Description**: Keep media at-rules at the bottom of the sheet.  
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/)   
**Violations**: Violations occur when a media at-rule appears before a ruleset.  
**Actions**: Find every media at-rule; check if the following rule is a ruleset   

---
**Description**: Within the groups the properties should be ordered alphabetically.  
**Source**: [Drupal](https://www.drupal.org/node/1887862)   
**Violations**: Violations occur when two properties from one group are not ordered alphabetically.  
**Actions**: Find every pair of properties that are next to each other and belong to the same group; check if they are alphabetically ordered  

---
**Description**: Order vendor-prefixed values by their version. Newer versions of vendor values should appear after old ones.  
**Source**: [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS)   
**Violations**: Violations occur when from two adjacent values, the first have a newer version than the second.  
**Actions**: Find every pair of adjacent vendor-prefixed values; check if the first value has a newer version than the second one

---
**Description**: Multiselectors with more than four selectors are not allowed.  
**Source**: [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS)   
**Violations**: Violations occur when a multi selector comprises more than four selectors.  
**Actions**: Find multiselectors that contain more than four selectors  

---
**Description**: Selectors with more than four simpleselectors are not allowed.  
**Source**: [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS)   
**Violations**: Violations occur when a selector comprises more than four simpleselectors.  
**Actions**: Find selectors that contain more than four simpleselectors      

---
**Description**: Put one space between the media feature and the value.
**Source**: [Drupal](https://www.drupal.org/node/1887862)
**Violations**: Violations occur when there is not exactly one space between the media feature and the value.
**Actions**: Find adjacent media feature and value; ensure there is one space between them

---
**Description**: Border-radius*-* properties should be top-left, top-right, bottom-right, bottom-left order.
**Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/)
**Violations**: Violations occur when the border properties are not ordered in the specified way.
**Actions**: Find every pair of the border properties within a ruleset; check if the properties do not conform to the specified order

---
**Description**: All text files should end with a single blank line.  
**Source**: [Drupal](https://www.drupal.org/node/1887862)     
**Violations**: Violations occur when a file does not end up with a blank line.  
**Actions**: Check whether the stylesheet ends with a newline symbol
