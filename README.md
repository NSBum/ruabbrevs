# ruabbrevs

This little utility collects template names from a [listing](https://ru.wiktionary.org/wiki/Справка:Условные_сокращения) of templates used on pages in ru.wiktionary.org and adds these template names to a database. These are used to markup Russian monolingual definitions that I extract elsewhere. For example, let's assume that I have the definition for the word _надмножество_: 

_матем. множество, для которого существует подмножество, когда каждый элемент подмножества является элементом надмножества; символ ⊇, ⊃_

When marking up the definition, we want to display the abbreviation _матем._ in italics as Wiktionary does. Since there are many such abbreviations used as templates on the site, we can build and maintain a database of them. That is what this little utility does. 
