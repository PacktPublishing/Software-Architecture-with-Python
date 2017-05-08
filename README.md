# Spatial Analytics with ArcGIS
This is the code repository for [Spatial Analytics with ArcGIS](https://www.packtpub.com/application-development/spatial-analytics-arcgis?utm_source=github&utm_medium=repository&utm_campaign=9781787122581), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
Spatial statistics has the potential to provide insight that is not otherwise available through traditional GIS tools. This book is designed to introduce you to the use of spatial statistics so you can solve complex geographic analysis.


## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.

Building ERP Solutions with Microsoft Dynamics NAV

Chapters 1,2, and 8 does not have codes in it. 

The code bundle provided by the author is not chapterwise.


The code will look like the following:
```
 ozone.file = system.file("extdata",    
    "ca_ozone_pts.shp", package="arcgisbinding") 
    d = arc.open(ozone.file) 
    cat('all fields: ', names(d@fields, fill = TRUE)         
    #print all fields
```

To complete the exercises in this book, you will need to have installed ArcGIS for Desktop 10.2 or higher with the Basic, Standard, or Advanced license level. We recommend that you use ArcGIS Desktop 10.4 or 10.5. In addition to this, you will also need to install R. Instructions for installing R are provided in Chapter 7, Introduction to the R Programming Language.

## Related Products
* [ArcPy and ArcGIS – Geospatial Analysis with Python](https://www.packtpub.com/application-development/arcpy-and-arcgis-–-geospatial-analysis-python?utm_source=github&utm_medium=repository&utm_campaign=9781783988662)

* [Mastering ArcGIS Server Development with JavaScript](https://www.packtpub.com/application-development/mastering-arcgis-server-development-javascript?utm_source=github&utm_medium=repository&utm_campaign=9781784396459)

* [Building Web Applications with ArcGIS](https://www.packtpub.com/application-development/building-web-applications-arcgis?utm_source=github&utm_medium=repository&utm_campaign=9781783552955)

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSe5qwunkGf6PUvzPirPDtuy1Du5Rlzew23UBp2S-P3wB-GcwQ/viewform) if you have any feedback or suggestions.
