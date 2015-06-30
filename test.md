
 **Description**: When possible, use em instead of pix   
 **Source**: [phpied](http://www.phpied.com/css-coding-conventions/)  
 **Violations**: Usage of unit with value px. For example, the snippet `font-size: 12pt;` is a violation. The snippet `font-size: 1em;` does not violate the convention.  
 **Actions**:  Recognize units with value px  
 
 **Description**: Avoid using z-indexes when possible   
 **Source**: [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS)  
 **Violations**: Usage of z-index property. Sample violation is the following `z-index: 100;`  
 **Actions**:  Recognize property with value z-index    
 
 **Description**: Avoid using !important   
 **Source**: [MediaWiki](https://www.mediawiki.org/wiki/Manual:Coding_conventions/CSS)  
 **Violations**: Usage of !important. Sample violation is the following `color: red !important;`  
 **Actions**:  Recognize usage of !important    
 
 **Description**: Do not use id selectors  
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-IDs-in-selectors), [Realdeal](http://www.realdealmarketing.net/docs/css-coding-style.php)  
 **Violations**:  Both sources require a warning whenever an id is found. An example of violation are `.mybox #go;`, `#header a` and `#mybox`  
 **Actions**:  Recognize usage of id selectors   
 
 **Description**: Disallow @import  
 **Source**: [CSS lint](https://github.com/CSSLint/csslint/wiki/Disallow-%40import), [Realdeal](http://www.realdealmarketing.net/docs/css-coding-style.php)  
 **Violations**:  Due to performance reasons, the usage of @import should be avoided. The following pattern is considered a warning `@import url(foo.css);`  
 **Actions**:  Recognize usage of @import statements   

 **Description**: If you must use an id selector (#selector) make sure that you have no more than one in your rule declaration    
 **Source**: [GitHub](http://primercss.io/guidelines/#css)  
 **Violations**:  The guideline states that if a selector contains an id, it should not contain any other simple-selecotrs. Thus, a rule like `#header .search #quicksearch { ... }` is a violation. Note however, that the convention does not apply to multi-selectors, i.e. the following css code is not a violation: `#header, #footer { ... }`  
 **Actions**:  Recognize selectors and ids; ensure selectors that contain ids contain only one id  
 
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
 **Actions**:  Recognize declarations, units with value rem, units with value px; recognize declarations with value that includes rem units; ensure existance of a declaration immediately before a given declaration; compare property names of declarations; ensure the value of declaration contains a px unit.  
 
 **Description**: CSS files must not include any @charset statements    
 **Source**: [Drupal](https://www.drupal.org/node/1887862)  
 **Violations**: Presence of charset atrule at the beginning of the CSS file: `@charset "UTF-8";`  
 **Actions**:  Recognize @charset statements  
 
 **Description**: Omit the protocol from embedded resources    
 **Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#Protocol)  
 **Violations**: Omit the protocol portion (http:, https:) from URLs pointing to images and other media files, style sheets, and scripts unless the respective files are not available over both protocols. Omitting the protocol—which makes the URL relative—prevents mixed content issues and results in minor file size savings. The snippet `url(http://www.google.com/images/example)` is a violation. The snippet `url(//www.google.com/images/example)` is not considered a violation.  
 **Actions**:  Recognize uri values; ensure the value of a uri does not start with a given string  
 
 **Description**:  the protocol from embedded resources    
 **Source**: [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml#Protocol)  
 **Violations**: Omit the protocol portion (http:, https:) from URLs pointing to images and other media files, style sheets, and scripts unless the respective files are not available over both protocols. Omitting the protocol—which makes the URL relative—prevents mixed content issues and results in minor file size savings. The snippet `url(http://www.google.com/images/example)` is a violation. The snippet `url(//www.google.com/images/example)` is not considered a violation.  
 **Actions**:  Recognize uri values; ensure the value of a uri does not start with a given string