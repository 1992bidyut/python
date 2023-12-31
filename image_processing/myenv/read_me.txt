Prerequisites:
* Install Homebrew:
    * /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"   
* Install Dependencies:
    * brew install cmake pkg-config ffmpeg   
Build OpenCV with FFmpeg in a Virtual Environment:
* Create and Activate Virtual Environment:
    * python3 -m venv myenv source myenv/bin/activate   
* Install Dependencies within the Virtual Environment:
    * pip install numpy matplotlib   
* Clone OpenCV and OpenCV Contrib Repositories:
    * git clone https://github.com/opencv/opencv.git 
    * cd opencv 
    * git clone https://github.com/opencv/opencv_contrib.git cd opencv_contrib 
    * git checkout <OPENCV_VERSION> 
    * cd ..   
* Build OpenCV:
    * mkdir build 
    * cd build 
    * cmake -D CMAKE_BUILD_TYPE=RELEASE \ -D CMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") \ -D INSTALL_C_EXAMPLES=OFF \ -D INSTALL_PYTHON_EXAMPLES=OFF \ -D OPENCV_GENERATE_PKGCONFIG=ON \ -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules \ -D BUILD_EXAMPLES=OFF \ -D WITH_FFMPEG=ON .. 
    * make -j$(sysctl -n hw.physicalcpu)   
* Install OpenCV:
    * sudo make install   
* Verify Installation:
    * pkg-config --modversion opencv4 pkg-config --libs opencv4 | grep ffmpeg    
Replace <OPENCV_VERSION> with the desired version of OpenCV. Adjust paths and configurations based on your system if needed.