# Shift Start Point

*Filter > Shift Start Point* moves the start point to the following on-curve node.

## Custom Parameter
 
You can have the filter run at export time with a custom parameter. This can be useful for automatically fixing interpolations. To do so, go to *File > Font Info > Exports,* select an instance, add a *Custom Parameter* with the plus button, choose *Filter* from the menu that pops up, and write `ShiftStartPoint` in the filter value. 

You can add the optional `steps:` attribute followed by the amount of node positions the start point should shift. Remember, as with all parameters, you can add `exclude:` or `include:` keywords followed by a comma-separated list of glyph names. E.g.:

    ShiftStartPoint; steps: 2; include: E, F, R

## Installation

*Shift Start Point* is [available in the Glyphs&nbsp;3 Plugin Manager](glyphsapp3://showplugin/Shift%20Start%20Point). Click on the *Install* button next to it and restart Glyphs.

# License

Copyright 2022 Rainer Erich Scheichelbauer (@mekkablue). Builds on template code by Georg Seifert (@schriftgestalt) and Jan Gerner (@yanone). Help for the conversion into the plug-in by Rainer Erich Scheichelbauer (@mekkablue).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
