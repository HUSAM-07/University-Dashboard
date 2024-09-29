
# University Dashboard and Navigation System

## Overview

This project is a comprehensive web application designed for students at BITS Pilani, Dubai Campus. It includes features for generating personalized timetables, navigating the campus, and accessing various university resources. The application is built using Python with Streamlit for the frontend and leverages several data processing and visualization libraries.

## Key Components

1. **Home Page (Home.py)**
   - Main dashboard interface
   - Navigation to different sections (University Resources, Clubs Resources)
   - Embedded resources like library catalog, LMS, and ERP systems

2. **Timetable Generator (2_Time Table Generator.py)**
   - Interactive form for selecting academic year, semester, and discipline
   - PDF timetable upload and processing
   - Course selection and constraint application
   - Dynamic timetable generation and visualization

3. **BPDC Navigator (3_BPDC Navigator.py)**
   - Campus navigation system
   - Building selection for start and end points
   - Path finding and distance calculation
   - Visual representation of the route on a map

4. **Map and Navigation Classes**
   - MapBuilder: Creates and manages the campus map
   - PathFinder: Implements path finding algorithms
   - BuildingProcessor: Handles building data and visualization
   - PointProcessor: Manages path points and graph structure

## Key Features

- **Personalized Timetable Generation**: Students can create custom timetables based on their course selections and preferences.
- **Interactive Campus Navigation**: Provides optimal routes between campus buildings with distance and time estimates.
- **Resource Integration**: Centralizes access to various university systems and resources.
- **Dynamic Visualization**: Utilizes Folium for map-based visualizations and custom styling for timetables.

## Technical Details

- **Languages**: Python
- **Key Libraries**: Streamlit, Folium, Pandas, NumPy, PyMuPDF, Tabula
- **Data Formats**: GeoJSON for map data, PDF for timetable input
- **Algorithms**: A* algorithm for pathfinding

## Usage

1. **Timetable Generation**:
   - Select academic year, semester, and discipline
   - Upload timetable PDF
   - Choose courses and sections
   - Apply constraints if needed
   - Generate and download personalized timetable

2. **Campus Navigation**:
   - Select start and end buildings
   - View the optimal path, distance, and estimated time

3. **Resource Access**:
   - Navigate through different sections to access university and club resources

## Future Enhancements

- Integration with more disciplines and academic programs
- Real-time updates for timetable changes
- Mobile app version for easier on-the-go access
- Integration with university event calendar

This application serves as a comprehensive tool for BITS Pilani Dubai students, streamlining academic planning and campus navigation while providing easy access to essential university resources.
