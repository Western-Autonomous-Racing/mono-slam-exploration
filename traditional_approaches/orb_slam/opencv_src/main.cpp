#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>

// file to confirm c++ is working
// to compile with opencv
// g++ main.cpp -o main `pkg-config --cflags --libs opencv4`
using namespace cv;
int main()
{
    std::string image_path = "/home/formatspecifier/Projects/mono-slam-exploration/traditional_approaches/.images/TestImage1.jpg";
    Mat img = imread(image_path, IMREAD_COLOR);

    imshow("Display window", img);
    int k = waitKey(0); // Wait for a keystroke in the window
    return 0;
}