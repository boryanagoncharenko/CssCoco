
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
 **Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#Protocol)  
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
 
 
 
 
 
 
 