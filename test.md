
 **Description**: When possible, use em instead of pix   
 **Source**: [phpied](http://www.phpied.com/css-coding-conventions/)  
 **Violations**: Usage of unit with value px. For example, the snippet `font-size: 12pt;` is a violation. The snippet `font-size: 1em;` does not violate the convention.  
 **Actions**:  Recognize units with value px  
 
---
 **Description**: Avoid using z-indexes when possible   
 **Source**: [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS)  
 **Violations**: Usage of z-index property. Sample violation is the following `z-index: 100;`  
 **Actions**:  Recognize property with value z-index    
 
---
 **Description**: Avoid using !important   
 **Source**: [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS)  
 **Violations**: Usage of !important. Sample violation is the following `color: red !important;`  
 **Actions**:  Recognize usage of !important    
 
---
 **Description**: Do not use id selectors  
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-IDs-in-selectors), [Realdeal](http://www.realdealmarketing.net/docs/css-coding-style.php)  
 **Violations**:  Both sources require a warning whenever an id is found. An example of violation are `.mybox #go;`, `#header a` and `#mybox`  
 **Actions**:  Recognize usage of id selectors   
 
---
 **Description**: Disallow @import  
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-%40import), [Realdeal](http://www.realdealmarketing.net/docs/css-coding-style.php)  
 **Violations**:  Due to performance reasons, the usage of @import should be avoided. The following pattern is considered a warning `@import url(foo.css);`  
 **Actions**:  Find usage of @import statements   

---
 **Description**: If you must use an id selector (#selector) make sure that you have no more than one in your rule declaration    
 **Source**: [GitHub](http://primercss.io/guidelines/#css)  
 **Violations**:  The guideline states that if a selector contains an id, it should not contain any other simple-selecotrs. Thus, a rule like `#header .search #quicksearch { ... }` is a violation. Note however, that the convention does not apply to multi-selectors, i.e. the following css code is not a violation: `#header, #footer { ... }`  
 **Actions**:  Recognize selectors and ids; check if selectors with ids contain othe simple selectors  
 
---
 **Description**: Use rem units preceded by px units for a safe fallback    
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
 **Actions**:  Recognize declarations, units with value rem, units with value px; find declarations with value that includes rem units; check if a declaration exists immediately before a given declaration; compare property names of declarations; check if the value of declaration contains a px unit.  
 
---
 **Description**: CSS files must not include any @charset statements    
 **Source**: [Drupal](https://www.drupal.org/node/1887862)  
 **Violations**: Presence of charset atrule at the beginning of the CSS file: `@charset "UTF-8";`  
 **Actions**:  Find @charset statements  
 
---
 **Description**: Omit the protocol from embedded resources    
 **Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#Protocol)  
 **Violations**: Omit the protocol portion (http:, https:) from URLs pointing to images and other media files, style sheets, and scripts unless the respective files are not available over both protocols. Omitting the protocol—which makes the URL relative—prevents mixed content issues and results in minor file size savings. The snippet `url(http://www.google.com/images/example)` is a violation. The snippet `url(//www.google.com/images/example)` is not considered a violation.  
 **Actions**:  Recognize uri values; check if the value of a uri starts with a given string  
 
---
 **Description**: Beware of box model size (rule 1)   
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-IDs-in-selectors)  
 **Violations**: In case the ruleset contains the box-sizing property, no warnings are yielded. However, if it does not contain the property, a warning should be issued if the any of the following couples of properties are found:
 1. width, border
 2. width, border-left
 3. width, border-right
 4. width, padding
 5. width, padding-left
 6. width, padding-right

**Actions**:  Find rulesets that does not contain the box-sizing property; check if they contain the property width and any of the properties in the list [border, border-left, border-right, padding, padding-left, padding-right].  

---
**Description**: Beware of box model size (rule 2)   
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-IDs-in-selectors)  
 **Violations**: In case the ruleset contains the box-sizing property, no warnings are yielded. However, if it does not contain the property, a warning should be issued if the any of the following couples of properties are found:
 1. height, border
 2. height, border-top
 3. height, border-bottom
 4. height, padding
 5. height, padding-top
 6. height, padding-bottom

**Actions**:  Find rulesets that does not contain the box-sizing property; check if they contain the property height and any of the properties in the list [border, border-top, border-bottom, padding, padding-top, padding-bottom].

---
**Description**: Require properties appropriate for display (rule 1)    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Require-properties-appropriate-for-display)  
 **Violations**: A warning is issued when `display: inline` used with width, height, margin, margin-top, margin-bottom, and float. The following snippet is considered a violation:
 ```
 .mybox {
    display: inline;
    height: 25px;
}
 ```
 **Actions**:  Recognize rulesets, declarations with specific properties and values; find rulesets containing a declaration with property display and value inline; chech if they contain any of the properties on the list [width, height, margin, margin-top, margin-bottom, float]     

---
**Description**: Require properties appropriate for display (rule 2)    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Require-properties-appropriate-for-display)  
 **Violations**: A warning is issued when a ruleset contains a declaration `display: inline-block` and a declaration with property float. The following snippet is considered a violation:display: 
 ```
 .mybox {
    display: inline-block;
    float: left;
}
 ```
 **Actions**:  Recognize rulesets, declarations with specific properties and values; find rulesets containing a declaration with property display and value inline-block; check if they contain a declaration with property float.     

---
**Description**: Require properties appropriate for display (rule 3)    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Require-properties-appropriate-for-display)  
 **Violations**: A warning is issued when a ruleset contains a declaration `display: block` and a declaration with property `vertical-align`. The following snippet is considered a violation:display: 
 ```
 .mybox {
    display: block;
    vertical-align: text-top;
}
 ```
 **Actions**:  Recognize rulesets, declarations with specific properties and values; find rulesets containing a declaration with property display and value block; check if they contain a declaration with property vertical-align.     
 
 ---
**Description**: Require properties appropriate for display (rule 4)    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Require-properties-appropriate-for-display)  
 **Violations**: A warning is issued when a ruleset contains a declaration with property display and value in the form table-\* and also contains declaration with property margin, margin-top, margin-right, margin-bottom or margin-left. The following snippet is considered a violation: 
 ```
 .mybox {
    display: table-cell;
    margin: 10px;
}
 ```
**Actions**:  Recognize rulesets, declarations with specific properties and value in a given form; find rulesets containing a declaration with property display and value that matches the form table-\*; check if it contains a declaration with any of the properties in the list [margin, margin-top, margin-right, margin-bottom, margin-left].     

---
**Description**: Disallow duplicate properties (rule 1)    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-duplicate-properties)  
 **Violations**: A warning is issued when a ruleset contains a given declaration twice, i.e. when the property and the value are identical. The following snippet is considered a violation: 
 ```
 .mybox {
    border: 1px solid black;
    border: 1px solid black;
}
 ```
 **Actions**:  Compare couples of declarations within a rule; check if the two declarations have equal properties and values.     

---
**Description**: Disallow duplicate properties (rule 2)    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-duplicate-properties)  
 **Violations**: A warning is issued when a ruleset contains a property twice and the two instances are separated by at least one other property. The following snippet is considered a violation: 
 ```
 .mybox {
    border: 1px solid black;
    color: green;
    border: 1px solid red;
}
 ```
 **Actions**:  Compare triples of declarations within a rule; check if the first and third have the same property and if the first and the second have different properties.     
 
 ---
**Description**: Disallow empty rules    
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
 **Actions**:  Recognize rulesets and declarations; determine whether a ruleset contains a declaration
 
    
---
**Description**: Disallow empty rules    
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
 **Actions**:  Recognize rulesets and declarations; determine whether a ruleset contains a declaration  

---
**Description**: Disallow adjoining classes    
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
 **Actions**:  Find two classes that are immediate siblings  

---
**Description**: Disallow the box-sizing property    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**: Usage of box-sizing property. Sample violations are:
 ```
.mybox {
    box-sizing: border-box;
}
```
 **Actions**:  Find box-sizing property
 
---
**Description**: Require compatible vendor prefixes    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**: A warning is issues when a vendor-prefixed property is missing. For example, the following ruleset is missing transform properties with -moz, -o and -ms prefixes:
 ```
.mybox {
    -webkit-transform: translate(50px, 100px);
}
```
 **Actions**:  Find vendor-specific properties; check whether the rule that holds them also contains all other vendor-prefixed properties.
  


---
**Description**: Disallow negative indent    
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

 **Actions**:  Find declarations with property text-indent and negative value; check whether the rule that holds them also contains a declaration of direction with value ltr.  

---
**Description**: Require standard property with vendor prefix    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**: A warning is issued when a vendor-prefixed property is used without a standard property after it. Sample violations are:
 ```
/* missing standard property */
.mybox {
    -moz-border-radius: 5px;
}
```
Note that there might be more than one vendor prefixes. In such cases the standard property should appear after the last vendor-prefixed property.
 **Actions**:  Find vendor-prefixed properties; check whether the following declaration does not exist; check whether the following declaration is not of the same property group.  
 
 ---
**Description**: Require a fallback color (rule 1)    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**: A warning is issued when a color property with a rgba(), hsl(), or hsla() color is used without a preceding color property that has an older color format, i.e. hexadecimal, named, or rgb(). Sample violations are:
 ```
.mybox {
    color: rgba(100, 200, 100, 0.5);
}
```
 **Actions**:  Find declarations with color property and rgba, hsl or hsla value; check if a previous declaration exists; check if the previous declaration has property color and value of type hex, color-name, rgb.  
 
 ---
**Description**: Disallow the star hack    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**: A warning is issued when a property is preceded with an asterisk.
 ```
.mybox {
    border: 1px solid black;
    *width: 100px;
}
```
 **Actions**:  Find properties that start with an asterisk. 
 
 ---
**Description**: Disallow the underscore hack    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**: A warning is issued when a property is preceded with an underscore.
 ```
.mybox {
    border: 1px solid black;
    _width: 100px;
}
```
 **Actions**:  Find properties that start with an underscore. 
 
 ---
**Description**: Bulletproof font face    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**: A warning is issued if the first URL declaration does not contain the suffix '?#iefix'.
 ```
@font-face {
    font-family: 'MyFontFamily';
    src: url('myfont-webfont.eot') format('embedded-opentype')
}
```
The implementation provided by CSS lint does not have much in common with the description. Testing shows that instead of ensuring that the first url has the required suffix, CSS lint checks in the font-face rule contains a url with the required suffix. In fact, the following CSS code avoids the mentioned bug, but does not comply with the definition of the rule.
```
@font-face {
  font-family: 'MyWebFont';
  src: url('webfont.eot'); /* IE9 Compat Modes */
  src: url('webfont.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
       url('webfont.woff2') format('woff2'), /* Super Modern Browsers */
}
```
In conclusion, a violation occurs when a font-face rule does not contain a url with the suffix '?#iefix'. 
 **Actions**:  Find font-face statements; check they contain a url with the required suffix.  
  
 ---
**Description**: Don't use too many web fonts    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**: A warning is issued when a stylesheet contains more than five @font-face declarations.
 **Actions**:  Recognize @font-face declarations; count the occurrences of @font-face declarations; compare the number to a predefined value.  
 
 ---
**Description**: Disallow selectors that look like regular expressions    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
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
 **Actions**:  Find any of selectors following selectors: *=, |=, ^=, $=, ~=  
 
 ---
**Description**: Disallow the universal selector    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
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
 **Actions**:  Find universal selector that is also the key simple-selector of a selector.  
 
 ---
**Description**: Disallow unqualified attribute selectors    
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
 **Actions**:  Find attribute selector that is also the key simple-selector of a selector.  
 
 ---
**Description**: Disallow overqualified elements    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**: A violation occurs when an html tag and class name are used together. However, the cases when two different elements are found with the same class name are not considered violations.
 ```
/* violation */
li.active { ... }

/* OK */
li.active { ... }
p.active { ... }
 ```
 **Actions**:  Find tags that are immediate siblings of classes. Count the number of unique tags that quality each class. Check if the number is equal to 1.
 
 ---
**Description**: Avoid qualifying ID and class names with type selectors    
 **Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#Protocol), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/)  
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
 **Actions**:  Find html tags that are immediate siblings of classes or ids.
 
 ---
**Description**: Disallow duplicate background images    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**:  The rule forbids the same URL for background image to be included twice in the stylesheet. Sample violations include:
 ```
.heart-icon {
    background: url(sprite.png) -16px 0 no-repeat;
}
.task-icon {
    background: url(sprite.png) -32px 0 no-repeat;
}
 ```
 **Actions**:  Check whether the URL values in background declarations are unique
 
 ---
**Description**: Disallow too many floats    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**:  Violations of this convention occur when a stylesheet contains more than 10 declarations of float
 **Actions**:  Count the number of occurrences of float; compare the number to 10
 
 ---
**Description**: Don't use too many font size declarations    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**:  Violations of this convention occur when a stylesheet contains more than 10 declarations of font-size.
 Note that the implementation provided by CSS lint takes into consideration only font-size declarations. Font declarations are disregarded.
 **Actions**:  Count the number of occurrences of font-size; compare the number to 10
 
---
**Description**: Disallow outline:none (rule 1)    
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
 Note that the implementation provided by CSS lint takes into consideration the presence of the :focus pseudo selector anywhere in the selector. Thus, a rule `a:focus p` does not yield a warning. Also, CSS lint does not check multiselectors. The rule `a:focus, p` is considered OK, which is obivously wrong.
 **Actions**:  Find rulesets that contain declaration with specific property and value; check if the selector of the ruleset contains the :focus pseudoselector.
 
 ---
**Description**: Disallow outline:none (rule 2)    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**:  Violations of this convention occur when a rule contains declaration outline: none or outline: 0 and a :focus pseudo selector, but does not contain any other declarations.
 ```
a:focus {
    outline: 0;
}
 ```
 **Actions**:  Find rulesets that contain declaration with specific property and value and the :focus pseudoselector; check they contain more than one declaration.
 
 ---
**Description**: Disallow qualified headings    
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**:  Violations of this convention occur when a ruleset contains a selector where the heading element is key and the selector contains more simple-selectors.
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
 **Actions**:  Find selectors that have html tags as key selectors; check whether the selectors contain other simple selectors
 
 ---
**Description**: Headings should only be defined once    
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
Note that CSS lint simply disregards the headings with pseudoselectors. Repeating the h3:hover selector in multiple rules does not yield a warning.
 **Actions**:  Find key selectors that contain headings and do not contain pseudoselectors; check if two key-selectors contain the same heading.
 
 ---
**Description**: Headings should only be defined once    
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
 **Actions**:  Find declarations with property background-image and gradient value; check if a previous declaration exists; check if the previous declaration has a background-color property.  
 
 ---
**Description**: Strings should use double quotes    
 **Source**: [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Drupal](https://www.drupal.org/node/1887862), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/)  
 **Violations**:  Violations of this convention occur when string uses single quotes:
 ```
 font-family: "Arial Black"
 ```
 **Actions**:  Find strings; check if they use single quotes
 
 ---
**Description**: Use single quotation marks for attribute selectors    
 **Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Drupal](https://www.drupal.org/node/1887862), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/)  
 **Violations**:  The convention refers to the values of attribute selectors. According to the [CSS specification](http://www.w3.org/TR/css3-selectors/#attribute-selectors), the values of attribute selectors can be CSS identifiers or strings. This the possible violations of this convention includes 1) using double quotes or 2) not using quotes at all:
 ```
 span[class=example]
 span[class="example"]
 ```
 **Actions**:  Find attribute values; check if their type is string; check if they use double quotes
 
 ---
**Description**: Use double quotation marks in charsets    
 **Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes)  
 **Violations**:  Using single quotes in charset is illegal according to CSS rules. Since the convention describes an anti-pattern, its violations occur when single quotes are using in a charset:
 ```
 @charset 'UTF-8';
 ```
 **Actions**:  Find strings in charsets; check if they use single quotes
 
 ---
**Description**: Use single quotes in values    
 **Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes)  
 **Violations**:  Violations occur when values contain strings that use double quotes:
 ```
 font-family: "Arial Black";
 ```
 **Actions**:  Find strings in values; check if they use double quotes
 
  ---
**Description**: Font names with spaces must surrounded by double quotes    
 **Source**: [WordPress](https://make.wordpress.org/core/handbook/coding-standards/css/) 
 **Violations**:  Font names appear in font or font-family declarations. Thus, a violation of this convention is a single-quote string that appears as a value of either of the declarations:
 ```
 font-family: 'Arial Black';
 ```
 **Actions**:  Find strings in values of declarations with properties 'font-family' or 'font'; check if they use single quotes

 ---
**Description**: Do not use over-qualified selectors    
 **Source**: [WordPress](https://make.wordpress.org/core/handbook/coding-standards/css/)  
 **Violations**:  Violations occur when an html tag appears immediately before a class or an id:
 ```
 div.container
 ```
 **Actions**:  Find html tags that are immediate siblings of a class or an id
 
 ---
**Description**: Don’t qualify ID rules with tag names or classes    
 **Source**: [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS)  
 **Violations**:  The convention states that if a rule has an ID selector as its key selector, tags should not be added to the rule. Violations include:
 ```
button#backButton {…}
.menu-left#newMenuIcon {…}
 ```
 **Actions**:  Find an id that is also a key selector; check if the previous sibling is an html tag
 
 ---
**Description**: Don’t qualify class rules with tag names or classes    
 **Source**: [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS)  
 **Violations**:  The convention states that if a rule has an class selector as its key selector, tags should not be added to the rule. Violations include:
 ```
treecell.indented {…}
 ```
 **Actions**:  Find a class that is also a key selector; check if the previous sibling is an html tag
 
 ---
**Description**: Use the most specific category possible    
 **Source**: [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS)  
 **Violations**:  The convention states that the single biggest cause of slowdown is too many rules in the tag category. Thus, instead of using tags as key selectors, we should use classes or ids. Violations include:
 ```
treeitem[mailfolder="true"] > treerow > treecell {…}
 ```
 **Actions**:  Find html tags that are also key selectors
 
 ---
**Description**: Avoid the descendant selector    
 **Source**: [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/)  
 **Violations**:  Violations of this guideline are the usages of the descendant selector:
 ```
treehead treerow treecell {...}
 ```
 **Actions**:  Find descendant selector
 
  ---
**Description**: Avoid using the child selector with tag category rules    
 **Source**: [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS)  
 **Violations**:  Violations of this convention are the selectors that have html tags as key selectors and contain a child selector:
 ```
treehead > treerow > treecell {...}
 ```
 **Actions**:  Find selectors that have html tags as their key selectors; check whether these selectors contain a child selector
 
 ---
**Description**: Question all usages of the child selector    
 **Source**: [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/)  
 **Violations**:  A warning should be raised when the child selector is used:
 ```
treeitem[IsImapServer="true"] > treerow > .tree-folderpane-icon {…}
 ```
 **Actions**:  Find child selector
 
  ---
**Description**: Avoid vendor-specific features unless necessary    
 **Source**: [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS)  
 **Violations**:  A warning should be issued when a vendor-specific property is found:
 ```
-webkit-border-radius
-moz-border-radius
 ```
 **Actions**:  Find properties that are vendor-prefixed  
 
 ---
**Description**: Put a semicolon at the end of each declaration  
 **Source**: [phpied](http://www.phpied.com/css-coding-conventions/), [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Drupal](https://www.drupal.org/node/1887862), [CSSguidelines](http://cssguidelin.es/#introduction)  
 **Violations**:  CSS allows the delimiter after the last declaration of a rule to be omitted. Since this can cause maintainability issues, the contanion requires the delimiter after the last declaration to be present. Violations occur when the last declaration of a rule does not have a following delimiter.
 ```
.myclass{
  color: red;
  font-family: "Arial Black"
}
 ```
 **Actions**:  Find the last declaration of a ruleset; check if there is a declaration delimiter after it
 
  ---
**Description**: Do not use shorthand properties, except border    
 **Source**: [phpied](http://www.phpied.com/css-coding-conventions/)  
 **Violations**:  A warning should be issued when any of the properties are encountered: margin, padding, background, font, list-style, transition.
 **Actions**:  Find properties that match the list [margin, padding, backgruond, font, list-style, transition]  
 
 ---
**Description**: Do not put quotes in uri values    
 **Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Drupal](https://www.drupal.org/node/1887862), [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS#.21important)   
 **Violations**:  A warning should be issued when the value of a URL is of type string:
 ```
 url("//www.google.com/css/maia.css")
 ```
 **Actions**:  Find url values; check if their type is string
 
 ---
**Description**: Use hex or rgba() for colors    
 **Source**: [GitHub](http://primercss.io/guidelines/#css), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/)  
 **Violations**:  Violations include usages of color-names, rgb(), hsl() and hsla():
 ```
 color: red;
 color: rgb(50, 100, 150)
 ```
 **Actions**:  Find color-names, rgb, hsl, or hsla  
 
 ---
**Description**: Use rgba only when opacity is needed    
 **Source**: [GitHub](http://primercss.io/guidelines/#css), [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/)  
 **Violations**:  Violations are usages of rgba() with last argument equal to 1:
 ```
 background-color: rgba(255, 0, 0, 1);
 ```
 **Actions**:  Find rgba() values with opacity equal to 1  
 
 ---
**Description**: Use short hex    
 **Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Idiomatic CSS](https://github.com/necolas/idiomatic-css), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [Drupal](https://www.drupal.org/node/1887862)  
 **Violations**:  Presence of hex that is long and could be shortened. Long hex values contain 6 hexadecimal characters and short - 3 characters. Long hex values that could be shortened match the format #rrggbb. For example, the following two values are violations:
```
#99EE11;
#ffffff;
```
The next examples do not violate the convention:
```#9E1;
#fff;
#E9E9E9
```
 **Actions**:  Find hex values that match the format #rrggbb  
 
 ---
**Description**: Use the shorthand margin property    
 **Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**:  Violation of this convention is a rule that contains all four properties: margin-top, margin-right, margin-bottom, margin-left.
```
a {
margin-top: 10px;
margin-right: 15px;
margin-bottom: 25px;
margin-left: 15px;
}
 **Actions**:  Find rulesets that contain all four properties in the list [margin-top, margin-right, margin-bottom, margin-left]  
 
  ---
 **Description**: Use the shorthand padding property    
 **Source**: [Wordpress](https://make.wordpress.org/core/handbook/coding-standards/css/), [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#type_Attributes), [CSS lint](https://github.com/CSSLint/csslint/wiki/Rules)  
 **Violations**:  Violation of this convention is a rule that contains all four properties: padding-top, padding-right, padding-bottom, padding-left.
```
a {
padding-top: 10px;
padding-right: 15px;
padding-bottom: 25px;
padding-left: 15px;
}
 **Actions**:  Find rulesets that contain all four properties in the list [padding-top, padding-right, padding-bottom, padding-left]  