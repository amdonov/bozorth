cmake_minimum_required (VERSION 2.6)
project (bozorth)
include_directories("/usr/include/glib-2.0" "/usr/lib64/glib-2.0/include"
       	"/usr/include/nbis" "/usr/java/default/include" 
	"/usr/java/default/include/linux" .)
link_directories(/usr/lib64/nbis)
FIND_PACKAGE(SWIG REQUIRED)
INCLUDE(${SWIG_USE_FILE})
SET(CMAKE_SWIG_FLAGS -package "com.bah.biometrics")
SWIG_ADD_MODULE(libbozorth java bozorth.i bozorth.c)
SWIG_LINK_LIBRARIES(libbozorth bozorth3)
install(FILES libbozorth.so DESTINATION usr/lib64)
install(FILES bozorth.jar DESTINATION usr/share/java)

