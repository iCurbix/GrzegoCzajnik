# GrzegoCzajnik
IMPORTANT - right now every face must be a triangle! If you use blender to export your objects just tick 'Triangulate faces' option.

IMPORTANT2 - right now .obj file must contain only one object

It is a simple python script that allows you to convert .obj file to c header file containing vertex count (NameOfTheFileVertexCount), vertex positions (NameOfTheFileVertices), vertex normals (NameOfTheFileNormals) / face normals (depends on how was .obj file exported, going to change a script a little so that you get both), texturing coordinates (NameOfTheFileTexCoords). Then you can easely use it for OpenGL.
For now, for the script to work you need to have .obj file in the same directory. After running the script you should write a filename of your .obj file (without an extension) and just press enter.
Not really convenient to use right now but gets the job done for me. Going to make it more comfortable to use in the future.
