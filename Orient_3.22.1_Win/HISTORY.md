# History

3.22.1.9 (2023-07-22)
* Fixed bug in Coulomb Stress calculation that was not reporting a solution.
* Added "Use friction" (PhiF) option to Coulomb Stress dialog to toggle use of kinematic versus dynamic axes.
* Removed "Dynamic" option from Spherical Projection Kinematics pane (use "Use friction" option).
* Removed "Dynamic" option from Statistics dialog (use "Use friction" option).
* Fixed ArcCos(c) error in LineToRake calculation when c > 1.0 due to roundoff error.

3.22.0.20 (2023-05-24)

* Fixed bug in stress tensor calculation introduced in 3.14. The Blenkinsop (2006) example again matches the results tabulated in the User Manual.
* Added slope stability daylight envelope. 
* Added slope stability friction cone. 
* Added slope stability lateral limits. 
* Added calculate intersections command.
* Added data dip symbol and dip ray to spherical plots.
* Added maxima dip symbol and dip ray to spherical plots.
* Added arrowheads to data, mean, and median circular histogram rays.
* Compiler update.
* No longer checks for updates due to new OS requirements for SSL installation. 
* Graphics library update.

3.21.0.20 (2023-03-04)

* Fixes to HSL color gradient using circular interpolation. 
* Improved speed of color gradient rendering using colormaps.
* Fixed errors in moment triangle contouring.
* Fixed bug in color scale bar to display levels.
* Added default colormap: sinusoid.
* Added standard colormaps: jet, rainbow, autumn, hot, cool. 
* Added new colormaps: turbo, coolwarm, blackbody.
* Added perceptually uniform colormaps: viridis, plasma, magma, inferno, cvidis.
* Renamed transparent color gradients from AR, AB, etc, to TR, TB, etc.
* Added WR linear color gradient
* Consolidated Spherical projection - Contours and Gridding panes.
* Added "Fill contours" option to Moment Triangle plot.
* Added "Fill contours" option to Ternary plot.
* Renamed "PGR - Contour" to "PGR - Fabric Index".
* Added "Fill contours" to "PGR - Fabric Index".
* Changed "PGR - Fabric Index - Interval" to "PGR - Fabric Index - Levels".
* Removed "Zero minimum" option.

3.20.0.27 (2023-01-07)

* Fixed errors reading dextral and sinistral fault sense.
* Simplified options for fault slip sense.
* Additional fixes to fault slip sense indication.
* Plunges now remain positive for fault slip lineations. 
* Made calculation of line rake optional.
* Numerous updates to User Manual.

3.19.0.15 (2022-11-27)

* Added spherical projection shading.
* Added spherical polygon filling.
* Enabled Undo for spherical projection rotation. 
* Added animated spherical projection rotation, with save to gif and png frames.

3.18.0.13 (2022-09-20)

* Compiler update.
* Fixes to girdle clustering.
* Added modifiable N labels to spherical and circular plots.
* Fixed bug in elliptic cone polygon.
* Added rotation of projection to elliptic cone axis.
* Added rotation of projection maxima to -Z.
* Fixed bug in display of linked moment tensor confidence cones.

3.17.0.57 (2022-08-28)

* Increased speed of clustering.
* Added density based clustering.
* Added fuzzy k-means clustering.
* Added von Mises-Fisher kappa computation using Bessel functions.
* Added calculation of Kent large kappa and beta parameters.
* Added lookup table for Watson kappa.
* Added lookup table for Bingham kappas.
* Added user manual section on parameter estimation.
* Added log output of orientation matrix.
* Changed "Generate Data" command to "Simulate Data".
* Added random simulation for Fisher distribution.
* Added random simulation for Watson distribution.
* Added random simulation for Kent distribution.
* Added rotation of spherical projections and rotation plots using keyboard.
* Rewrite of circular KDE with fixes and new estimation methods (Taylor and ROT).
* Rewrite of circular histogram section in user manual.

3.16.0.18 (2022-05-21)

* Fixed output of upper hemisphere results in 'Calculate Best-Fit' command'.
* Added MLE Watson kappa to Statistics.
* Added output of clustering silhouette minimum in Log.
* Removed image flattening which was causing undesired effects.
* Rewrote example for axis cluster partitioning using Pmax and silhouette.
* Rewrote example for vector cluster partitioning using Pmax and silhouette.
* Added normalized cluster "Max" for (maximized) value (instead of "Cost").
* Sine^2 is now used instead of sine for axis similarity in cluster analysis.
* Added distance-based cluster partitioning.
* Added shortcuts for "Cluster Analysis", "Calculate Lines", and "Statistics".
* Modified cluster analysis to initialize seed using distance. 
* "New Plot View" now copies plot and type preferences from previous plot view.
* Added 95% "Cone" option for spherical projection data, for resample data.

3.15.0.64 (2022-03-02)

* Minor updates to circular uniformity tests.
* Added spherical Rayleigh uniformity test. 
* Added 'Theta' (longitude sphere) and 'Phi' (colatitude) column headers.
* Updated circular median reporting of duplicate medians.
* Added median symbol and ray to circular histogram.
* User Manual is now a separate download.
* Added Help menu command to open User Manual.
* Added linked LS and PT orientation matrices.
* Added bootstrapping of linked LS and PT orientation matrices.
* Clean up of dead code.
* Separate executables for Macintosh M1 (Amd) and Intel.
* Separate executables for Linux Amd and Intel.
* Removed symmetric bootstrap confidence cone from Log.
* Removed Circular and Ring options for small circle confidence.
* Beachball now drawn for only one domain, as selected in Kinematics pane.
* Moment Triangle plots can now plot by domain.
* New icon.
* Fixed "Find" function for Triangular Moment plots with multiple domains.
* The "Cursor Symbols" dialog now includes settings to display P, T, and M axes. 
* Fixed display bug where paint and symbol pickers were not refreshing.
* Fixed display bugs in circular histogram grid.
* Added radial bin lines separate from major radial grid.
* Fixed spherical plot "Cursor Symbols" to account for domains. 
* Added optional display of L,S,P,T,M symbols, and S,M arcs to spherical plot "Cursor Symbols".
* Fixes to Dark Theme display.
* Fixed bug in circular median.
* Added linked LS and PT statistics to Log.
* Added focal mechanism categories to moment triangle plot.
* Fixes to moment triangle plot.
* Changed Google Maps "Show Location" command to drop a pin.
* Kinematic tangent lines displayed by domain.
* Kinematic tangent lines require S or L visible (see manual).
* Now reads FaultKin tab delimited txt files, and TR, TL, NR, NL kinematic Sense.
* Now reads DEX, SIN, NOR, REV kinematic Sense.
* Added signed rake option.
* Fixed possible reserved characters (<, >, &) in kml description text.
* Added a "Change Domains" command to set or swap domain ids.
* Fixes to SVG export.
* Gradient bitmaps are now flattened in vector files.
* Fixes to EPS export.

3.14.0.20 (2021-07-30)

* Rewrote clustering function, fixed bug occurring when 0 points were found in a cluster.
* Fixed bug in 'Open Preferences' command.
* Renamed 'Save Preferences' and 'Open Preferences' commands to 'Save Template' and 'Open Template'. 
* Updated GUI components.
* Extensive code refactoring.
* Fixed bug in display of data small circles.
* Fixed bug in visibility of rotation frame axes. 
* Data for rotation frames on spherical projections is now automatically orthonormalized.
* Rewrote Copy/Cut/Paste to use tab separated headers. Copy and paste from spreadsheets must include the header row. Only visible columns are copied.
* File Open command now utilizes same code as Paste.
* Fixed contouring of PGR plot.
* Added "Classify Weights" command.
* Circular data statistics now give a warning if estimated values of kappa are to small to calculate a reliable confidence interval, but report the values.
* Added circular data kernel density estimation.
* Added circular median.
* Added reporting of critical Rbar values for Rayleigh uniformity test.
* Added circular p-statistic for Rayleigh uniformity test. 

3.13.0.30 (2021-01-23)

* Fixed display bug in sphere maxima settings.
* Added digitizing of latitude, longitude for map symbols.
* Google Earth KML export now supports domains (D1, D2, ...) and kinematic elements M, P, and T.
* Rewrote JSON preferences export.
* Better enforced minimum sample sizes for statistics, fixing errors with small sample sizes.
* Now allows limiting of directional elements and domains in statistics log. 
* The map 'Scale factor' is replaced by 'X scale' and 'Y scale' to allow separate scaling of X and Y, as when using lat long for X and Y.
* Removed spherical 'Hull' confidence in favor of covariance ellipse.
* Added fitting of spherical ellipses (elliptic cones).
* Added frame (line in plane) orientation statistics for SL and PT frames. 
* Fixed bug that was not displaying moment triangle if the data had no 'Type' values.
* Added saving and opening of preferences independent of data files.

3.12.0.25 (2020-06-13)

* All plots now have symbols "Visible" options for a data type, and a "Hide All" button to hide all data types. This makes it easier to select one data type.
* All data type options are now stored by list. This solves problems with multiple plot views and lists with identical types. These are stored in a "Lists" folder. The "Types" folder is no loner used.
* Map subdomain maxima export now includes "Zone". 
* Map domain search now correctly handles multi-subdomain selections.
* Map domain search now correctly ignores domain 0.
* Map domain search allows selection of domain 0 with "Search" set to 0.
* Map has new seed fill algorithm to determine if domains are connected, domain 0 does not need to remain connected.
* Map tick mark Labels can now be scaled, for example to convert UTM in meters to kilometers.
* PGR plot now has option "Global" to include all open data sets.
* PGR plot now has option "Eigenvalue data" to read eigenvalues from a file.
* PGR plot now has options to plot "Intensity" and "Density" fabric index contours and color gradients.
* PGR plot and Spherical projections now have options to color code symbol fills based on "Weight" or "Domain" using a color gradient.
* PGR plots now can have contouring of Bingham test values (intensity).
* PGR plots now have contouring and gradient of fabric indexes I, IP, D, and DP. 
* PGR plots now can plot eigenvalues imported in data files.
* PGR added fabric density and fabric density protolith indexes.
* Plots no longer zoom out when refreshing.
* Compton stress inversion now has options to maximize P (equivalent to maximizing e1) as well as to maximize B (equivalent to minimizing e3).
* Localization is no longer used for the decimal separator, it is always a period. Comma separators caused numerous bugs issues in file input and output.
* Fixed clipping and masking bugs in svg output of triangular diagrams.
* Added Bingham uniformity test.
* Numerous Cocoa bugs fixed in Mac version.
* Numerous stability fixes.
* Extensive revision of user manual.

3.11.1.8 (2020-01-05)

* Fixed status bar display bug on Mac.
* Modified display colors of spreadsheet.
* Statistics command now shows values for a single measurement, allowing determination of P and T or kinematic or dynamic stress directions from a single fault.
* Fixed potential range error for ArcCos in uniformity tests.
* Additional bug fixes.

3.11.0.16 (2019-12-09)

* Fixed introduced bug preventing input of latitude, longitude.
* Fixed display of some angles not converting from radians to degrees.
* Added Terzaghi fracture survey weighting corrections.  
* Fixed several bugs in the data entry grid.
* Added ternary plots.
* Added contouring and gradient fill to ternary and moment tensor plots using kernel density estimation.
* Added ability to change labels on PGR, ternary, and moment tensor plots.
* Added the option to plot hidden symbols using a dot option.
* Modifications to better handle exceptions for preference files.
* Added tests of uniformity.
* Renamed Probability density plot Kernel density estimate (KDE) plot, since Kamb is also a probability density estimate.
* Added spherical projection equal probability contours.
* Added MUD contour interval for KDE plot.
* Fixed some edit boxes that were not allowing decimal point entry.

3.10.3.6 (2019-09-17)

* Fixes to bugs in Macintosh controls, including scrolling issues.
* Renamed and expanded Number Format dialog, angles, latitude-longitude, and coordinate digits of precision can now be set globally. Note that the displayed digits will be the same as is written to a file.
* Fixes to localization settings using commas for decimal places. 

3.10.2.1  (2019-08-16)

* Fixes for High DPI  Windows 150% and 200% modes, including new icon sets.
* Fixes to allow localization by country of decimal separators other than decimal point. Files use decimal point separators.

3.10.1.4 (2019 -07-29)

* Numerous fixes to support Windows multiple DPI modes.
* New toolbar icons at multiple resolutions for multiple DPI modes.
* Fixes to opacity and gradient pickers, and symbols menus.
* Numerous additional fixes, for screen display and other issues.

3.10.0.23 (2019-07-07)

* Added selective display of one or two quadrants to circular histograms.
* Changed column header “Comment” to “Notes” following StraboSpot. “Comments” and “Note” are both valid input headers, output header is “Notes”. 
* Find function in spherical projection window now correctly ignores hidden data types.
* Display bug fix to GradientPicker.
* Fixed bug in Rake to Rake AR conversion causing error when not assigned.
* Rake to Rake AR conversion now automatically updates plots. 
* Numerical labels can now be displayed with negative numbers, ±0..180, as well as 0..360.
* Added vertical component and dip histogram plots.
* Added rake plots.
* Restore Defaults command now correctly removes Lists and Types directories. Old copies are backed up with a timestamp.
* Fixes to Orientation Units dialog display.
* Added moment tensor triangle plot.
* Added option to disable/enable weighting in circular histogram.

3.9.1.4 (2019–05-02)

* Fixed bug in number formats in spreadsheet export.
* Added Waze map to Data Show Location commands.
* Added Coperix map to Data Show Location commands.
* Added Coperix satellite to Data Show Location commands.
* Added MapQuest map to Data Show Location commands.
* Added MapQuest satellite to Data Show Location commands.
* Updated IDE version.
* Fixes to Macintosh components.
* Fixed bug when reopening open but empty data list (untitled).

3.9.0.23 (2019-03-24)

* Preference files are now JSON instead of XML. Old preference files are updated as accessed.
* Fixes to MacOS version.
* Updated Here Maps location search.
* Added warning dialog to Calculate Lines command.
* Made 'Helvetica, Arial, Liberation Sans, sans-serif' the default svg font family. Note that some versions of Adobe Illustrator (e.g., Macintosh CS6 and Windows CS5) contain bugs and will not open svg files with fonts it does not recognize. 
* StraboSpot import integration added.
* Added tick marks to orientation map.
* Added symbol set with centered dot.
* Added tick marks and labels to orientation map.
* Added UpDown controls to Type change ComboBoxes.
* Fixed error in opening symbol preferences.
* Fixed and modified Project File opening and saving.
* Fixes to digitizing routines.

3.8.0.34 (2018-11-09)

* Added option to set minimum contour to zero.
* Added option for selection cursor to display planes.
* Fixes to PaintPicker control.
* Fixed bug in saving relative file paths of open files. If an error occurs when quitting the application with open files, restart EllipseFit and close and reopen all files.
* Renamed Calculate Maxima command to Calculate Best-Fit.
* Added calculation of best-fit plane to lines in Calculate Best-Fit. This can be used, for example, to calculate strike and true dip from apparent dips. 
* Added the ability to add data lines and planes interactively on spherical projections.
* Removed duplication of preference data in XML preference files. 
* Added Rotate Net command.
* Added Random Data command.
* Renamed Fibonacci Sphere command Fibonacci Grid.
* Modified Cluster Partitioning search to use a more uniform distribution (no discernible change in outcomes).
* Added stress inversion (see Stress Inversion).
* Added global, by spherical projection, switch to turn off weighting.
* Added dialog to select options in Data > Statistics log.
* Added Aki-Richards Rake AR option.
* Strike Left has been renamed Strike B (British). Data files with headers Strike Left or strikel will still be read correctly. Headers in saved files however will now be Strike B. 
* The Data Columns dialog now allows three states, visible, hidden, or visible if available.
* Fixes to Copy and Cut commands.

3.7.1.3 (2018-01-21)

* Fixed uninitialized font bug in Log window. If you have display problems in the Log window, use the Edit > Font command to select a monospace font of about 12 points.
* Fixed bug in dictionary that was not deleting the first item.
* Unused file preferences are now stored in the preferences directory and not loaded until needed.
* Unused type preferences are now stored in the preferences directory and not loaded until needed.
* Fixed bug in preferences dialog kinematics pane preventing beach ball selection. 
* New desktop icon. 

3.7.0.9 (2018-01-15)

* Added ability to display tick marks outside the perimeter of circular histograms and spherical projections.
* UTM command now only operates on selected rows.
* Fixed UTM conversion bug due to degree to radian conversion.
* Double clicking on a plot data point now opens the point data in the spreadsheet. 
* Added Data > Calculate Maxima command.
* Fixed bug causing offset of contours and mismatch with filled contour gradient.
* Fixed scale bar to display full range if Auto-range is off.
* Fixed rarely encountered bug in convex hull calculation.
* Added first order trend surface calculation, in Trend Surface command.
* Removed display of maxima and statistics for single data point.
* Made Data > Statistics command global.
* Added ability to hide Data cursor.
* Fixed bug in Plot Selected command.
* Added slip trend line option for kinematic analysis.
* Commands Statistics, Rotate Data, and Cluster Analysis can now be accessed from a plot window.
* Fixed bug so circular histogram plots now save preferences by file name, instead of globally.

3.6.3.3 (2017-02-23)

* Added troubleshooting start up option to hold down Option/Alt key to delete preferences. 
* Fixed bug causing intermittent platform-dependent floating point overflow when calculating a line the plane error.
* Fixed bug that occurred during kinematic analysis if not all data had lines and planes.

3.6.2.15 (2017-01-12)

* Multiple spherical projection plots can now be opened for each data set using the New Plot View command. These may be used to display different domains, hemispheres, or for other purposes.
* The positions of each spherical projection plot are saved and restored.
* The Windows menu now includes items for all plot windows.
* Fixed a bug in the Domain Search that prevented assigning domains. 
* The Domain Search now includes an Auto-assign option that automatically updates the data and all open plots with domains during a search.
* Added a Set button in the Domain Search preferences pane to sett the map extends from the data extents.
* Fixed the Domain Search Cancel button to restore previous domains.
* Fixed the Domain Search to keep the display of domains.
* Now saves subdomain configuration between sessions.
* Added a Scale factor for the map to convert latitude and longitude as a Mercator projection and correctly scale distances. 
* Fixed refresh bug in preferences dialog.
* Fixed symbol color bug in KML export.
* Turned off display of new map symbols when new domain is created during a domain search.
* Now the Domain column is correctly displayed when creating a new domain.
* Domain search index now updates correctly during manual editing.
* Added rectangular “marquee” selection to domain editing. 
* Changed domain 8 color from “cssAqua” to “cssGreen” (cssAqua = cssCyan).
* Domain colors are now displayed, and can be changed, in the Domain Search dialog.
* Added subdomain eigenfoliation or eigenlineation display to Orientation Map status bar, changed display in Spherical Projection status bar to match, 3 digits for theta values, 2 for phi values. 
* Added a Search All button to the Domain Search dialog. This does a sequential search through each current domain. 
* Project files now stripped of some uneeded file level settings.
* Extensive code refactoring.

3.6.0.15 (2016-12-11)

* SVG graphics file output now includes gradient and beachball bitmaps. SVG bitmaps are PNG format with an alpha channel (RGBA) to support transparency.
* EPS graphics file output now includes gradient and beachball bitmaps.	EPS bitmaps are uncompressed with three bytes per pixel (RGB, the EPS file format does not support transparency).
* Fixed EPS text justification.
* Fixed EPS bounding box.
* Added N label to spherical projections for the number of data points.
* Added option for a title to spherical projections.
* Fixed bug in contour limits for automatic range selection.
* Fixed opacity selection and gradient opacity bugs.
* Fixed bug in domain search weighting.
* Added 6 transparent to color (TR, TY, TG, TC, TB, TM) gradient presets. These allow multiple contour gradients in one plot. 
* The Calculate Lines from Rake command now only sets the Sense if one is already assigned (normal or reverse). The use of the Sense column for kinematic data is clarified in Section 8.2. 
* Circular Histogram settings are now saved by file name.
* Added N label to circular histograms for the number of data points.
* Added option for a title to circular histograms.
	
3.5.3.6 (2016-11-27)

* Now can undo Calculate Lines command. 
* Selection of data spreadsheet cell (0, 0) now toggles Select All/Select None.
* Rotate Data command now has Directed/Undirected option.
* Data planes rotated to a dip of zero (less than 1E-9 radians), so the Strike becomes undefined, now retain their previous Strike instead of an arbitrary value. 
* A great circle that represents a plane with a dip of zero (less than 1E-9 radians) plots as a circle instead of an arc. This occurs on either hemisphere. If it is obscured by the net frame, increase the stroke width, or decrease the opacity of the Frame (e.g., to 50%).
* A ray that represents an undirected line with a plunge of zero (less than 1E-9 radians) plots as a diameter instead of a radius. This occurs on either hemisphere. 
* A symbol that represents an undirected line with a plunge of zero (less than 1E-9 radians) plots as two diametrically opposed symbols. This occurs on either hemisphere. 
* Added Mirror option to turn on/off mirroring of horizontal data symbols.
* Fixed Undo command in Log Window.
* Fixed various cosmetic bugs, Gradient Dialog display, Linux button heights, Windows About dialog text display, etc.  
* Added display of intermediate eigenvector in status bar when selecting two or more data points, useful, for example, in determining the obtuse angle bisectors of fault pairs.
* Added display of intermediate eigenvector in spherical projection when selecting two or more data points, useful, for example, in determining the obtuse angle bisectors of fault pairs.
* Changed data cursor symbol to circle.
* Added Cursor Symbols dialog.
* Fixed bugs to correctly locating data points in status bar text and Find command in rotated projections.

3.5.2.12 (2016-11-13)

* Fixed some file opening and saving issues. 
* Fixed some row selection bugs.
* Added version update checking.
* Fixed display bugs in Opacity and Gradient dialogs.

3.5.1.1 (2016-11-02)

* Fixed row selection bug.
* Fixed data line/plane data display bug.
 
3.5.0.28 (2016-10-31)

* Changed messaging procedures from PostMessage to Dispatch message.
* Changed Graph menu item to Plot.
*  Fixed display bug, the data window was not reliably updating spreadsheet display. 
* Added ability to set angle precision for display and file saving.
* Added Edit metadata command to edit file metadata, initial lines in file beginning with “//”.
* Fixed Calculate Line from Rake.
* Removed Calculate Line from Plunge, as nonunique. 
* Column display is now stored by list.
* Added Link data column to link together data items.
* Fixed UTM to latitude, longitude conversion, changed units from radians to degrees.
* Fixed editing of integer values in spreadsheet, they now delete when expected.
* Added Calculate Line from Acute and Obtuse angle with linked plane.
* Fixed rare exception bug in Kent confidence cones.
* Reduced Data Statistics log output. Data types tagged as directed output: vector means, Fisher and Kent confidence. Data types tagged as undirected output: eigenvectors, Bingham and Watson confidence.
* Enabled Cut and Paste commands in spreadsheet.
* Enabled Undo for Cut and Paste and other commands.
* Enabled Save in addition to Save As command.
* Fixed status bar display of coordinates for non-local coordinate spherical projections and inverted X and Y.
* Added interactive and draggable spherical projection rotation using mouse.
* Eigenvectors now calculated using faster singular value decomposition instead of the Jacobi method.
* Added azimuthal equidistant projection.

3.4.2.3 (2016-06-11)

* Now allows a minimum spherical projection contour level of 0.
* Added automatic range setting for spherical projection contour grid, now the gradient automatically scales to full grid range by default.
* Added rescaling of spherical projection contour grid to expected uniform density to contour in multiples of uniform density.
* Added gradient scale bar option to spherical projection.
* Added WBGYR gradient preset.
* Added an option to place spherical net above the gradient or beachball bitmaps.
* Fixed rotation of spherical projection tick marks.

3.4.1.3 (2016-03-25)

* Fixed orientation map subdomain maxima symbol drawing bug.
* Fixed orientation map subdomain maxima symbol count bug.
* Centered orientation map on page.
* Changed orientation map status display from one to two decimal places.
* Moved orientation map maxima symbols above data symbols.
* Fixed reading and display of explicit NaN values and, therefore, display of polylines (such as the Modern Continental Outlines example data).  
* Fixed domain search bug failure to assign domains when multiple files were open.
* Added Apply button to Domain Search dialog.
* The visibility of symbols on the orientation map is no longer linked to their visibility on the spherical projection.
* Domain search subdomains are now saved and optionally displayed after Domain Search dialog is closed.
* Added an option in the Preferences dialog Orientation Map pane to show or hide the subdomains when Domain Search dialog is closed.

3.4.0.16 (2016-03-20)

* Bound Windows and Linux resources into executable.
* Optimized with FPC 3.0.0 and LCL 1.6.0.
* Improved memory management by freeing unused forms.
* Added View Image Window command, moved location of File Open Image command.
* Replaced Timers with IdleTimers for better performance.
* Settings for Rotate Data, Rotate Projection, and UTM Conversion are now stored between sessions.
* Consolidated raster and vector image saving under Export Image As command.
* Improvements to digitize commands.
* Added Kent distribution confidence cones.
* Added Kent statistics to Log output.
* Added Bingham statistics to Log output.
* Data input behavior now more spreadsheet compatible. Pressing Enter to accept input moves down, additional rows are always available for input, fixed bug causing a scroll up when on last data line.

3.3.3.11 (2016-02-03)

* Fixed Watson confidence cone weighting error, was dividing by count instead of weighted count.
* Added process cancelation code for lengthy operations in bootstrap routines.
* Added progress display status for lengthy operations in bootstrap routines.
* The preferences dialog now displays only the data types available in the current file, instead of all files.
* The spherical projection settings are now saved by file name, instead of globally.
* Only graphs of the current data are now redrawn, instead of all graphs.
* When selecting a plot window the associated file in the spreadsheet is now displayed.

3.3.2.9 (2016-01-24)

* Fixed Page Size dialog display failure.
* Fixed Replicates symbol picker display.
* Fixed several User Manual images in Chapter 6.
* Added Watson confidence cone data to Log.
* Watson confidence cones now rotate on projection rotation.
* Bingham confidence cones now rotate on projection rotation.
* Fixed preferences initialization bug.
* Preferences dialog now reopens on last panel.
* Preferences dialog now reopens with last data type selected.
* Weighting now works with Fisher confidence cones.
* Weighting now works with Watson confidence cones.
* Added translucent display of data polygons on hidden hemisphere.
* Fixed divide by zero bug.
* Fixed additional Windows and Linux control display issues. 
* No longer asks twice on quitting with modified file.
* Added translucent display of tangent lines on hidden hemisphere.
* Status bar now indicates if a file is modified.
* Can now display kinematic beachball and tangent lines at same time.

3.3.1.13 (2016-01-17)

* Fixed some dialog control display issues in Linux.
* Added translucent display of contour lines on hidden hemisphere.
* Added translucent display of confidence ellipses on hidden hemisphere.
* Fixed XML creator to correctly translate [&”<>] characters in file paths. Project files are validated XML.
* Project files now save open file paths.
* Added commands to save and open project files.
* Fixed bug causing crash when closing a tabbed window.
* Fixed bug that was naming “untitled” “untitled 1”.
* Fixed some tab orders and control spacing.
* Modified status bar display to include calculated angle for two selected data points. Clicking on the status bar toggles between line and plane units.

3.3.0.8 (2016-01-11)

* Corrected the name of the Calculate Line Orthorectify option to Orthonormalize.
* Changed Orthonormalize algorithm from QR decomposition to polar decomposition, to give the closest orthogonal frame. The difference should be minimal.
* Fixed sorting in Weight, Error, Rake, Sense, and Alpha columns.
* Tweaked the tangent-normal wrapping algorithm used in bootstrap covariance calculation. The difference should be minimal. 
* Plot windows now save their placement on the screen based on name.
* Added Cluster Partitioning, see User Manual Chapter 10.
* Added hidden small circle display.

3.2.1.4 (2016-01-02)

* Fixed numerous control display issues in Linux.
* Cleaned up control alignments in Preferences dialog.
* Fixed Beachball to rotate with projection.
* Modified small circle bootstrapping work with psi close to 90.
* Added small circle bootstrap estimation of confidence in psi.
* Added drawing of small circle bootstrap confidence rings about psi.
* Added Fibonacci Sphere command.
* Added opacity options to plot symbols, rays, and great circles on hidden hemisphere.
* Numerous updates to the user manual.

3.2.0.7 (2015-12-29)

* Added best-fit small circles.
* Modified labels in Columns Dialog to show current data angles, e.g., Strike.
* Fixed control spacing in Linux Calculate Lines dialog.
* Rotate Projection dialog now includes Vector Mean and Small Circle Pole.
* Added circular confidence cones for bootstrap means.
* Added Alpha field and plotting of small circle data.
* Added option to plot hidden directed data, on opposing hemisphere, with an unfilled symbol.
* Added Help Orient Home Page command.
* Fixed NaN entry and polyline markers, that got broken in 3.1.0.
* Cleaned up Log file, added Fisher statistics.

3.1.0.27 (2015-12-14)

* Added Sense column for kinematic analysis to allow undirected (downward) lineation entry, previously it was necessary to input directed (upward or downward) fault lineations. 
* Fixed weighting error in orientation field.
* Fixed orientation map page size setting.
* Added Weight column for data point weighting, 1 is the default value, 2 counts a data point twice, etc..
* Decreased non-splined points to 91 in spherical net small circles. Use Restore defaults to implement. 
* Fixed duplicate drawing of spherical net small circles.
* Spherical net great circles in SVG are now computed as cubic Bezier paths.
* Added Windows system tray icon
* Added encapsulated PostScript (EPS) vector graphics export.
* Added AutoCAD drawing exchange format (DXF) vector graphics export.
* Added hexagon and pentagon symbols.
* Fixed arrowheads in kinematic analysis plots.
* Clarified directional versus orientation data definitions.
* Added Rake column for the rake of a line in the containing plane.
* Added Error column giving the angular error between a line and the containing plane. Read only.
* Fixed data entry to not delete invalid entry over existing value.
* Fixed several data entry display issues.
* Added Calculate Line command to calculate line in plane angles from projection, trend, plunge or rake.
* Rotate Data command now rotates only selected items.
* Modified status bar to display maximum and minimum eigenvectors for two or more data points.
* Fixed command clicking on plots to update multiple selections in the spreadsheet.
* Removed Yahoo! Maps linking, they shut down this service. 
* Fixed bug setting X and Y fields when locating points.
* Added orthorectification option to Calculate Line command.
* Added bootstrapping analysis with elliptical confidence cones and polygon regions (hulls).
* Fixed Log Window Copy command. 

3.0.2.1 (2015-09-28)

* Fixed Preferences Dialog list spacing.
* Optimized contour line segment joining for vector export. 
* Optimized data grid scrolling.
* Fixed Linux About display.
* Optimized messaging.
* Fixed crash when non-Roman Unicode characters are in user name.  A workaround is to run Orient from a thumb drive with only Roman characters in file and folder names.
* Work on User Manual.

3.0.1.0 (2015-05-30)

* Fixed bug importing dip direction.

3.0.0.77 (2015-05-01)

* First release of Orient 3. Complete rewrite with numerous new features. Compiled, tested, and debugged on Macintosh, Windows, and Linux.

2.1.2 (2012-10-31)

* Last release of Orient 2.

2.0.0.7 (2006-07-23)

* First release of Orient 2. Complete rewrite with Macintosh, Windows, and Linux versions.

1.6.1 (1995-02-28)

* Last release of Orient 1.

1.0.0 (1986)

* First release of Orient 1, Microsoft DOS. Introduced modified Kamb contouring, triangular fabric plots, and automated domain analysis (see Vollmer, 1985, 1988, 1990, 1993, 1995). Available by download (modem) from COGSnet, sponsored by the Computer Oriented Geological Society, Denver, CO.

