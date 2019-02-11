#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : digikam
Version  : 6.0.0
Release  : 4
URL      : https://github.com/KDE/digikam/archive/v6.0.0.tar.gz
Source0  : https://github.com/KDE/digikam/archive/v6.0.0.tar.gz
Summary  : An advanced digital photo management application
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CDDL-1.1 CECILL-1.1 GPL-2.0 LGPL-2.1
Requires: digikam-bin = %{version}-%{release}
Requires: digikam-data = %{version}-%{release}
Requires: digikam-lib = %{version}-%{release}
Requires: digikam-license = %{version}-%{release}
Requires: digikam-man = %{version}-%{release}
BuildRequires : bison-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : doxygen
BuildRequires : eigen-dev
BuildRequires : exiv2-dev
BuildRequires : expat-dev
BuildRequires : extra-cmake-modules pkgconfig(glib-2.0)
BuildRequires : flex
BuildRequires : gettext-dev
BuildRequires : glibc-dev
BuildRequires : kcalcore-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kfilemetadata-dev
BuildRequires : kio-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-dev
BuildRequires : mesa-dev
BuildRequires : opencv-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(exiv2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(lensfun)
BuildRequires : pkgconfig(libgphoto2)
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtwebengine-dev
BuildRequires : ruby
BuildRequires : subversion
BuildRequires : threadweaver-dev
BuildRequires : tiff-dev

%description
The file Metadata manipulation Qt wrapper:
- containers : all metadata classes to group information by categories.
- engine     : the low level metadata extraction class based on Exiv2 API and managing :
* C++ exception from this library.
* All API call protected by a common mutex to fix non re-entrancy from Exiv2.
* All Exiv2 API are only used in this area to not expose all digiKam core classes of API changes.
- dmetadata  : the high level metadata class, based on metadata engine, but not based on Exiv2 API.
This class must be used everywhere in digiKam.

%package bin
Summary: bin components for the digikam package.
Group: Binaries
Requires: digikam-data = %{version}-%{release}
Requires: digikam-license = %{version}-%{release}
Requires: digikam-man = %{version}-%{release}

%description bin
bin components for the digikam package.


%package data
Summary: data components for the digikam package.
Group: Data

%description data
data components for the digikam package.


%package dev
Summary: dev components for the digikam package.
Group: Development
Requires: digikam-lib = %{version}-%{release}
Requires: digikam-bin = %{version}-%{release}
Requires: digikam-data = %{version}-%{release}
Provides: digikam-devel = %{version}-%{release}

%description dev
dev components for the digikam package.


%package lib
Summary: lib components for the digikam package.
Group: Libraries
Requires: digikam-data = %{version}-%{release}
Requires: digikam-license = %{version}-%{release}

%description lib
lib components for the digikam package.


%package license
Summary: license components for the digikam package.
Group: Default

%description license
license components for the digikam package.


%package man
Summary: man components for the digikam package.
Group: Default

%description man
man components for the digikam package.


%prep
%setup -q -n digikam-6.0.0
pushd ..
cp -a digikam-6.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549897834
mkdir -p clr-build
pushd clr-build
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%cmake .. -DENABLE_QWEBENGINE=TRUE
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
%cmake .. -DENABLE_QWEBENGINE=TRUE
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549897834
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/digikam
cp COPYING %{buildroot}/usr/share/package-licenses/digikam/COPYING
cp COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/digikam/COPYING-CMAKE-SCRIPTS
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/digikam/COPYING.LIB
cp core/libs/dimg/filters/greycstoration/cimg/LICENSE.txt %{buildroot}/usr/share/package-licenses/digikam/core_libs_dimg_filters_greycstoration_cimg_LICENSE.txt
cp core/libs/rawengine/libraw/COPYRIGHT %{buildroot}/usr/share/package-licenses/digikam/core_libs_rawengine_libraw_COPYRIGHT
cp core/libs/rawengine/libraw/LICENSE.CDDL %{buildroot}/usr/share/package-licenses/digikam/core_libs_rawengine_libraw_LICENSE.CDDL
cp core/libs/rawengine/libraw/LICENSE.LGPL %{buildroot}/usr/share/package-licenses/digikam/core_libs_rawengine_libraw_LICENSE.LGPL
cp core/tests/modeltest/LICENSE.GPL %{buildroot}/usr/share/package-licenses/digikam/core_tests_modeltest_LICENSE.GPL
cp core/utilities/assistants/webservices/common/o2/LICENSE %{buildroot}/usr/share/package-licenses/digikam/core_utilities_assistants_webservices_common_o2_LICENSE
cp core/utilities/mediaserver/upnpsdk/Platinum/LICENSE.txt %{buildroot}/usr/share/package-licenses/digikam/core_utilities_mediaserver_upnpsdk_Platinum_LICENSE.txt
cp project/bundles/macports/installer/GPL.txt %{buildroot}/usr/share/package-licenses/digikam/project_bundles_macports_installer_GPL.txt
cp project/bundles/mxe/installer/GPL.txt %{buildroot}/usr/share/package-licenses/digikam/project_bundles_mxe_installer_GPL.txt
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cleanup_digikamdb
/usr/bin/digikam
/usr/bin/digitaglinktree
/usr/bin/haswell/digikam
/usr/bin/haswell/showfoto
/usr/bin/showfoto

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.digikam.desktop
/usr/share/applications/org.kde.showfoto.desktop
/usr/share/digikam/about/css/bootstrap-theme.min.css
/usr/share/digikam/about/css/bootstrap.min.css
/usr/share/digikam/about/css/digikam.css
/usr/share/digikam/about/images/body-background.jpg
/usr/share/digikam/about/images/top-left-digikam.png
/usr/share/digikam/about/js/bootstrap.min.js
/usr/share/digikam/about/js/digikam.js
/usr/share/digikam/about/js/jquery.min.js
/usr/share/digikam/about/main.html
/usr/share/digikam/colorschemes/blackbody.colors
/usr/share/digikam/colorschemes/colorcontrast.colors
/usr/share/digikam/colorschemes/darkroom.colors
/usr/share/digikam/colorschemes/fusiongray.colors
/usr/share/digikam/colorschemes/graycard.colors
/usr/share/digikam/colorschemes/highkey.colors
/usr/share/digikam/colorschemes/lowkey.colors
/usr/share/digikam/colorschemes/shadeofgray.colors
/usr/share/digikam/colorschemes/sunsetcolor.colors
/usr/share/digikam/colorschemes/whitebalance.colors
/usr/share/digikam/data/assistant-enfuse.png
/usr/share/digikam/data/assistant-hugin.png
/usr/share/digikam/data/assistant-preprocessing.png
/usr/share/digikam/data/assistant-stack.png
/usr/share/digikam/data/assistant-tripod.png
/usr/share/digikam/data/banner-digikam.png
/usr/share/digikam/data/bluejean-texture.png
/usr/share/digikam/data/bothhorz.png
/usr/share/digikam/data/bothvert.png
/usr/share/digikam/data/bricks-texture.png
/usr/share/digikam/data/bricks2-texture.png
/usr/share/digikam/data/burlap-texture.png
/usr/share/digikam/data/canvas-texture.png
/usr/share/digikam/data/cellwood-texture.png
/usr/share/digikam/data/centerheight.png
/usr/share/digikam/data/centerwidth.png
/usr/share/digikam/data/chalk-pattern.png
/usr/share/digikam/data/colors-chromablue.png
/usr/share/digikam/data/colors-chromared.png
/usr/share/digikam/data/colors-luma.png
/usr/share/digikam/data/craters-pattern.png
/usr/share/digikam/data/curvefree.png
/usr/share/digikam/data/curvemooth.png
/usr/share/digikam/data/dried-pattern.png
/usr/share/digikam/data/duplicatebothhorz.png
/usr/share/digikam/data/duplicatebothvert.png
/usr/share/digikam/data/editimage.png
/usr/share/digikam/data/exifinfo.png
/usr/share/digikam/data/fabric-texture.png
/usr/share/digikam/data/granit-pattern.png
/usr/share/digikam/data/histogram-lin.png
/usr/share/digikam/data/histogram-log.png
/usr/share/digikam/data/histogram.png
/usr/share/digikam/data/ice-pattern.png
/usr/share/digikam/data/image-full.png
/usr/share/digikam/data/image-selection.png
/usr/share/digikam/data/leaf-pattern.png
/usr/share/digikam/data/logo-beta.png
/usr/share/digikam/data/logo-cimg.png
/usr/share/digikam/data/logo-digikam.png
/usr/share/digikam/data/logo-exiv2.png
/usr/share/digikam/data/logo-gphoto.png
/usr/share/digikam/data/logo-lcms.png
/usr/share/digikam/data/logo-piwigo.png
/usr/share/digikam/data/lut3d/bleach.png
/usr/share/digikam/data/lut3d/blue_crush.png
/usr/share/digikam/data/lut3d/bw_contrast.png
/usr/share/digikam/data/lut3d/instant.png
/usr/share/digikam/data/lut3d/original.png
/usr/share/digikam/data/lut3d/punch.png
/usr/share/digikam/data/lut3d/summer.png
/usr/share/digikam/data/lut3d/tokyo.png
/usr/share/digikam/data/lut3d/vintage.png
/usr/share/digikam/data/lut3d/washout.png
/usr/share/digikam/data/lut3d/washout_color.png
/usr/share/digikam/data/lut3d/x_process.png
/usr/share/digikam/data/marble-pattern.png
/usr/share/digikam/data/marble-texture.png
/usr/share/digikam/data/marble2-texture.png
/usr/share/digikam/data/metalwire-texture.png
/usr/share/digikam/data/modern-texture.png
/usr/share/digikam/data/moss-texture.png
/usr/share/digikam/data/original.png
/usr/share/digikam/data/paper-pattern.png
/usr/share/digikam/data/paper-texture.png
/usr/share/digikam/data/paper2-texture.png
/usr/share/digikam/data/parque-pattern.png
/usr/share/digikam/data/pine-pattern.png
/usr/share/digikam/data/pink-pattern.png
/usr/share/digikam/data/process-working.png
/usr/share/digikam/data/rain-pattern.png
/usr/share/digikam/data/rock-pattern.png
/usr/share/digikam/data/sample-aix.png
/usr/share/digikam/data/splash-digikam.png
/usr/share/digikam/data/stone-pattern.png
/usr/share/digikam/data/stone-texture.png
/usr/share/digikam/data/target.png
/usr/share/digikam/data/togglemouseover.png
/usr/share/digikam/data/wall-pattern.png
/usr/share/digikam/data/wall-texture.png
/usr/share/digikam/data/wood-pattern.png
/usr/share/digikam/database/dbconfig.xml
/usr/share/digikam/database/mysql-global.conf
/usr/share/digikam/facesengine/dlib_face_recognition_resnet_model_v1.dat
/usr/share/digikam/facesengine/haarcascade_frontalface_alt.xml
/usr/share/digikam/facesengine/haarcascade_frontalface_alt2.xml
/usr/share/digikam/facesengine/haarcascade_frontalface_alt_tree.xml
/usr/share/digikam/facesengine/haarcascade_frontalface_default.xml
/usr/share/digikam/facesengine/haarcascade_mcs_lefteye.xml
/usr/share/digikam/facesengine/haarcascade_mcs_mouth.xml
/usr/share/digikam/facesengine/haarcascade_mcs_nose.xml
/usr/share/digikam/facesengine/haarcascade_mcs_righteye.xml
/usr/share/digikam/facesengine/haarcascade_profileface.xml
/usr/share/digikam/facesengine/shapepredictor.dat
/usr/share/digikam/geoiface/backend-googlemaps-js.js
/usr/share/digikam/geoiface/backend-googlemaps.html
/usr/share/digikam/geoiface/cluster-circle-00ff00-selected.png
/usr/share/digikam/geoiface/cluster-circle-00ff00-someselected.png
/usr/share/digikam/geoiface/cluster-circle-00ff00.png
/usr/share/digikam/geoiface/cluster-circle-00ffff-selected.png
/usr/share/digikam/geoiface/cluster-circle-00ffff-someselected.png
/usr/share/digikam/geoiface/cluster-circle-00ffff.png
/usr/share/digikam/geoiface/cluster-circle-ff0000-selected.png
/usr/share/digikam/geoiface/cluster-circle-ff0000-someselected.png
/usr/share/digikam/geoiface/cluster-circle-ff0000.png
/usr/share/digikam/geoiface/cluster-circle-ff7f00-selected.png
/usr/share/digikam/geoiface/cluster-circle-ff7f00-someselected.png
/usr/share/digikam/geoiface/cluster-circle-ff7f00.png
/usr/share/digikam/geoiface/cluster-circle-ffff00-selected.png
/usr/share/digikam/geoiface/cluster-circle-ffff00-someselected.png
/usr/share/digikam/geoiface/cluster-circle-ffff00.png
/usr/share/digikam/geoiface/marker-00ff00-selected.png
/usr/share/digikam/geoiface/marker-00ff00-someselected.png
/usr/share/digikam/geoiface/marker-00ff00.png
/usr/share/digikam/geoiface/marker-00ffff-selected.png
/usr/share/digikam/geoiface/marker-00ffff-someselected.png
/usr/share/digikam/geoiface/marker-00ffff.png
/usr/share/digikam/geoiface/marker-ff0000-selected.png
/usr/share/digikam/geoiface/marker-ff0000-someselected.png
/usr/share/digikam/geoiface/marker-ff0000.png
/usr/share/digikam/geoiface/marker-ff7f00-selected.png
/usr/share/digikam/geoiface/marker-ff7f00-someselected.png
/usr/share/digikam/geoiface/marker-ff7f00.png
/usr/share/digikam/geoiface/marker-ffff00-selected.png
/usr/share/digikam/geoiface/marker-ffff00-someselected.png
/usr/share/digikam/geoiface/marker-ffff00.png
/usr/share/digikam/geoiface/marker-icon-16x16.png
/usr/share/digikam/geolocationedit/bookmarks-marker.png
/usr/share/digikam/geolocationedit/searchmarker-normal.png
/usr/share/digikam/geolocationedit/searchmarker-selected.png
/usr/share/digikam/metadata/topicset.iptc-subjectcode.xml
/usr/share/digikam/profiles/compatibleWithAdobeRGB1998.icc
/usr/share/digikam/profiles/prophoto.icm
/usr/share/digikam/profiles/srgb-d65.icm
/usr/share/digikam/profiles/widegamut.icm
/usr/share/digikam/templates/1_photo_10.5x14.8cm.desktop
/usr/share/digikam/templates/1_photo_10x15cm.desktop
/usr/share/digikam/templates/1_photo_20x25cm.desktop
/usr/share/digikam/templates/1_photo_8x10.desktop
/usr/share/digikam/templates/1_photo_9x13cm.desktop
/usr/share/digikam/templates/2_photos_13x18cm.desktop
/usr/share/digikam/templates/2_photos_5x7.desktop
/usr/share/digikam/templates/3_photos_10x15cm.desktop
/usr/share/digikam/templates/3_photos_4x6.desktop
/usr/share/digikam/templates/4_photos_10x13.33cm.desktop
/usr/share/digikam/templates/4_photos_3.5x5.desktop
/usr/share/digikam/templates/4_photos_4.5x5cm.desktop
/usr/share/digikam/templates/4_photos_9x13cm.desktop
/usr/share/digikam/templates/4x6Album.desktop
/usr/share/digikam/templates/6_photos_3.5x4.5cm.desktop
/usr/share/digikam/templates/6_photos_3.5x4cm.desktop
/usr/share/digikam/templates/8_photos_6x9cm.desktop
/usr/share/digikam/templates/Album-Collage.desktop
/usr/share/digikam/templates/Album-Collage1.desktop
/usr/share/digikam/templates/Album_10x15cm.desktop
/usr/share/digikam/templates/Album_11.5x15cm.desktop
/usr/share/digikam/templates/FullPage.desktop
/usr/share/digikam/templates/Photoframe.desktop
/usr/share/digikam/templates/TEMPLATE_HOWTO
/usr/share/digikam/templates/Thumbnails_5x4.desktop
/usr/share/digikam/templates/Thumbnails_6x5.desktop
/usr/share/digikam/templates/templates.xml
/usr/share/digikam/themes/THEME_HOWTO
/usr/share/digikam/themes/bluecurved/bluecurved.desktop
/usr/share/digikam/themes/bluecurved/body.png
/usr/share/digikam/themes/bluecurved/document-save.png
/usr/share/digikam/themes/bluecurved/go-next.png
/usr/share/digikam/themes/bluecurved/go-previous.png
/usr/share/digikam/themes/bluecurved/go-top.png
/usr/share/digikam/themes/bluecurved/gohome.png
/usr/share/digikam/themes/bluecurved/left.png
/usr/share/digikam/themes/bluecurved/preview.png
/usr/share/digikam/themes/bluecurved/style.css
/usr/share/digikam/themes/bluecurved/template.xsl
/usr/share/digikam/themes/bluecurved/vide.png
/usr/share/digikam/themes/blueframes/blueframes.desktop
/usr/share/digikam/themes/blueframes/preview.png
/usr/share/digikam/themes/blueframes/style.css
/usr/share/digikam/themes/blueframes/template.xsl
/usr/share/digikam/themes/classic/classic.desktop
/usr/share/digikam/themes/classic/gohome.png
/usr/share/digikam/themes/classic/preview.png
/usr/share/digikam/themes/classic/template.xsl
/usr/share/digikam/themes/classic/up.png
/usr/share/digikam/themes/cleanframes/black.css
/usr/share/digikam/themes/cleanframes/blue.css
/usr/share/digikam/themes/cleanframes/brown.css
/usr/share/digikam/themes/cleanframes/cleanframes.desktop
/usr/share/digikam/themes/cleanframes/green.css
/usr/share/digikam/themes/cleanframes/lavender.css
/usr/share/digikam/themes/cleanframes/pink.css
/usr/share/digikam/themes/cleanframes/preview.png
/usr/share/digikam/themes/cleanframes/red.css
/usr/share/digikam/themes/cleanframes/star.png
/usr/share/digikam/themes/cleanframes/template.xsl
/usr/share/digikam/themes/cleanframes/yellow.css
/usr/share/digikam/themes/dateframes/dateframes.desktop
/usr/share/digikam/themes/dateframes/preview.png
/usr/share/digikam/themes/dateframes/template.xsl
/usr/share/digikam/themes/details/details.desktop
/usr/share/digikam/themes/details/next.png
/usr/share/digikam/themes/details/next_disabled.png
/usr/share/digikam/themes/details/preview.png
/usr/share/digikam/themes/details/previous.png
/usr/share/digikam/themes/details/previous_disabled.png
/usr/share/digikam/themes/details/style.css
/usr/share/digikam/themes/details/template.xsl
/usr/share/digikam/themes/details/up.png
/usr/share/digikam/themes/elegant/elegant.desktop
/usr/share/digikam/themes/elegant/preview.png
/usr/share/digikam/themes/elegant/resources/css/dark.css
/usr/share/digikam/themes/elegant/resources/css/lytebox.css
/usr/share/digikam/themes/elegant/resources/css/master.css
/usr/share/digikam/themes/elegant/resources/css/natural.css
/usr/share/digikam/themes/elegant/resources/images/close_blue.png
/usr/share/digikam/themes/elegant/resources/images/close_gold.png
/usr/share/digikam/themes/elegant/resources/images/close_green.png
/usr/share/digikam/themes/elegant/resources/images/close_grey.png
/usr/share/digikam/themes/elegant/resources/images/close_red.png
/usr/share/digikam/themes/elegant/resources/images/loading.gif
/usr/share/digikam/themes/elegant/resources/images/next_blue.gif
/usr/share/digikam/themes/elegant/resources/images/next_gold.gif
/usr/share/digikam/themes/elegant/resources/images/next_green.gif
/usr/share/digikam/themes/elegant/resources/images/next_grey.gif
/usr/share/digikam/themes/elegant/resources/images/next_red.gif
/usr/share/digikam/themes/elegant/resources/images/pause_blue.png
/usr/share/digikam/themes/elegant/resources/images/pause_gold.png
/usr/share/digikam/themes/elegant/resources/images/pause_green.png
/usr/share/digikam/themes/elegant/resources/images/pause_grey.png
/usr/share/digikam/themes/elegant/resources/images/pause_red.png
/usr/share/digikam/themes/elegant/resources/images/play_blue.png
/usr/share/digikam/themes/elegant/resources/images/play_gold.png
/usr/share/digikam/themes/elegant/resources/images/play_green.png
/usr/share/digikam/themes/elegant/resources/images/play_grey.png
/usr/share/digikam/themes/elegant/resources/images/play_red.png
/usr/share/digikam/themes/elegant/resources/images/prev_blue.gif
/usr/share/digikam/themes/elegant/resources/images/prev_gold.gif
/usr/share/digikam/themes/elegant/resources/images/prev_green.gif
/usr/share/digikam/themes/elegant/resources/images/prev_grey.gif
/usr/share/digikam/themes/elegant/resources/images/prev_red.gif
/usr/share/digikam/themes/elegant/resources/js/lytebox.js
/usr/share/digikam/themes/elegant/template.xsl
/usr/share/digikam/themes/floatingcards/back.png
/usr/share/digikam/themes/floatingcards/floatingcards.desktop
/usr/share/digikam/themes/floatingcards/forward.png
/usr/share/digikam/themes/floatingcards/image_nav.js
/usr/share/digikam/themes/floatingcards/next.png
/usr/share/digikam/themes/floatingcards/prev.png
/usr/share/digikam/themes/floatingcards/preview.png
/usr/share/digikam/themes/floatingcards/style.css
/usr/share/digikam/themes/floatingcards/template.xsl
/usr/share/digikam/themes/floatingcards/up.png
/usr/share/digikam/themes/frames/frames.desktop
/usr/share/digikam/themes/frames/preview.png
/usr/share/digikam/themes/frames/style.css
/usr/share/digikam/themes/frames/template.xsl
/usr/share/digikam/themes/matrix/bg.png
/usr/share/digikam/themes/matrix/matrix.desktop
/usr/share/digikam/themes/matrix/preview.png
/usr/share/digikam/themes/matrix/style.css
/usr/share/digikam/themes/matrix/template.xsl
/usr/share/digikam/themes/s0/arrows_source.svg
/usr/share/digikam/themes/s0/next.png
/usr/share/digikam/themes/s0/next_disabled.png
/usr/share/digikam/themes/s0/preview.png
/usr/share/digikam/themes/s0/previous.png
/usr/share/digikam/themes/s0/previous_disabled.png
/usr/share/digikam/themes/s0/s0.desktop
/usr/share/digikam/themes/s0/style.css
/usr/share/digikam/themes/s0/template.xsl
/usr/share/digikam/themes/s0/up.png
/usr/share/digikam/themes/simple/dark.css
/usr/share/digikam/themes/simple/natural.css
/usr/share/digikam/themes/simple/preview.png
/usr/share/digikam/themes/simple/simple.desktop
/usr/share/digikam/themes/simple/template.xsl
/usr/share/digikam/themes/simplerounded/niftyCorners.css
/usr/share/digikam/themes/simplerounded/niftycube.js
/usr/share/digikam/themes/simplerounded/preview.png
/usr/share/digikam/themes/simplerounded/simplerounded.desktop
/usr/share/digikam/themes/simplerounded/template.xsl
/usr/share/digikam/themes/simpleslides/preview.png
/usr/share/digikam/themes/simpleslides/simpleslides.desktop
/usr/share/digikam/themes/simpleslides/template.xsl
/usr/share/digikam/themes/snow/next.png
/usr/share/digikam/themes/snow/next.svg
/usr/share/digikam/themes/snow/next_disabled.png
/usr/share/digikam/themes/snow/preview.png
/usr/share/digikam/themes/snow/previous.png
/usr/share/digikam/themes/snow/previous_disabled.png
/usr/share/digikam/themes/snow/snow.desktop
/usr/share/digikam/themes/snow/style.css
/usr/share/digikam/themes/snow/template.xsl
/usr/share/digikam/themes/vanilla/preview.png
/usr/share/digikam/themes/vanilla/resources/css/charcoal.css
/usr/share/digikam/themes/vanilla/resources/css/dusk.css
/usr/share/digikam/themes/vanilla/resources/css/graphite.css
/usr/share/digikam/themes/vanilla/resources/css/ice_blue.css
/usr/share/digikam/themes/vanilla/resources/css/ie6.css
/usr/share/digikam/themes/vanilla/resources/css/ie7.css
/usr/share/digikam/themes/vanilla/resources/css/ivory.css
/usr/share/digikam/themes/vanilla/resources/css/light_grey.css
/usr/share/digikam/themes/vanilla/resources/css/lytebox.css
/usr/share/digikam/themes/vanilla/resources/css/master.css
/usr/share/digikam/themes/vanilla/resources/css/midnight.css
/usr/share/digikam/themes/vanilla/resources/css/white_on_black.css
/usr/share/digikam/themes/vanilla/resources/images/close_blue.png
/usr/share/digikam/themes/vanilla/resources/images/close_gold.png
/usr/share/digikam/themes/vanilla/resources/images/close_green.png
/usr/share/digikam/themes/vanilla/resources/images/close_grey.png
/usr/share/digikam/themes/vanilla/resources/images/close_red.png
/usr/share/digikam/themes/vanilla/resources/images/loading.gif
/usr/share/digikam/themes/vanilla/resources/images/next_blue.gif
/usr/share/digikam/themes/vanilla/resources/images/next_gold.gif
/usr/share/digikam/themes/vanilla/resources/images/next_green.gif
/usr/share/digikam/themes/vanilla/resources/images/next_grey.gif
/usr/share/digikam/themes/vanilla/resources/images/next_red.gif
/usr/share/digikam/themes/vanilla/resources/images/pause_blue.png
/usr/share/digikam/themes/vanilla/resources/images/pause_gold.png
/usr/share/digikam/themes/vanilla/resources/images/pause_green.png
/usr/share/digikam/themes/vanilla/resources/images/pause_grey.png
/usr/share/digikam/themes/vanilla/resources/images/pause_red.png
/usr/share/digikam/themes/vanilla/resources/images/play_blue.png
/usr/share/digikam/themes/vanilla/resources/images/play_gold.png
/usr/share/digikam/themes/vanilla/resources/images/play_green.png
/usr/share/digikam/themes/vanilla/resources/images/play_grey.png
/usr/share/digikam/themes/vanilla/resources/images/play_red.png
/usr/share/digikam/themes/vanilla/resources/images/prev_blue.gif
/usr/share/digikam/themes/vanilla/resources/images/prev_gold.gif
/usr/share/digikam/themes/vanilla/resources/images/prev_green.gif
/usr/share/digikam/themes/vanilla/resources/images/prev_grey.gif
/usr/share/digikam/themes/vanilla/resources/images/prev_red.gif
/usr/share/digikam/themes/vanilla/resources/js/lytebox.js
/usr/share/digikam/themes/vanilla/resources/js/pngfix.js
/usr/share/digikam/themes/vanilla/resources/misc/shadow-grid.gif
/usr/share/digikam/themes/vanilla/resources/misc/shadow.png
/usr/share/digikam/themes/vanilla/template.xsl
/usr/share/digikam/themes/vanilla/vanilla.desktop
/usr/share/digikam/utils/digikam-camera
/usr/share/icons/hicolor/128x128/apps/digikam.png
/usr/share/icons/hicolor/128x128/apps/expoblending.png
/usr/share/icons/hicolor/128x128/apps/panorama.png
/usr/share/icons/hicolor/128x128/apps/showfoto.png
/usr/share/icons/hicolor/16x16/apps/digikam.png
/usr/share/icons/hicolor/16x16/apps/dk-box.png
/usr/share/icons/hicolor/16x16/apps/dk-dropbox.png
/usr/share/icons/hicolor/16x16/apps/dk-facebook-white.png
/usr/share/icons/hicolor/16x16/apps/dk-facebook.png
/usr/share/icons/hicolor/16x16/apps/dk-flickr.png
/usr/share/icons/hicolor/16x16/apps/dk-googledrive.png
/usr/share/icons/hicolor/16x16/apps/dk-googlephoto.png
/usr/share/icons/hicolor/16x16/apps/dk-imageshack.png
/usr/share/icons/hicolor/16x16/apps/dk-imgur.png
/usr/share/icons/hicolor/16x16/apps/dk-ipfs.png
/usr/share/icons/hicolor/16x16/apps/dk-mediawiki.png
/usr/share/icons/hicolor/16x16/apps/dk-onedrive.png
/usr/share/icons/hicolor/16x16/apps/dk-pinterest.png
/usr/share/icons/hicolor/16x16/apps/dk-piwigo.png
/usr/share/icons/hicolor/16x16/apps/dk-rajce.png
/usr/share/icons/hicolor/16x16/apps/dk-smugmug.png
/usr/share/icons/hicolor/16x16/apps/expoblending.png
/usr/share/icons/hicolor/16x16/apps/panorama.png
/usr/share/icons/hicolor/16x16/apps/showfoto.png
/usr/share/icons/hicolor/22x22/apps/digikam.png
/usr/share/icons/hicolor/22x22/apps/dk-box.png
/usr/share/icons/hicolor/22x22/apps/dk-dropbox.png
/usr/share/icons/hicolor/22x22/apps/dk-facebook-white.png
/usr/share/icons/hicolor/22x22/apps/dk-facebook.png
/usr/share/icons/hicolor/22x22/apps/dk-flickr.png
/usr/share/icons/hicolor/22x22/apps/dk-googledrive.png
/usr/share/icons/hicolor/22x22/apps/dk-googlephoto.png
/usr/share/icons/hicolor/22x22/apps/dk-imageshack.png
/usr/share/icons/hicolor/22x22/apps/dk-imgur.png
/usr/share/icons/hicolor/22x22/apps/dk-ipfs.png
/usr/share/icons/hicolor/22x22/apps/dk-mediawiki.png
/usr/share/icons/hicolor/22x22/apps/dk-onedrive.png
/usr/share/icons/hicolor/22x22/apps/dk-pinterest.png
/usr/share/icons/hicolor/22x22/apps/dk-piwigo.png
/usr/share/icons/hicolor/22x22/apps/dk-rajce.png
/usr/share/icons/hicolor/22x22/apps/dk-smugmug.png
/usr/share/icons/hicolor/22x22/apps/expoblending.png
/usr/share/icons/hicolor/22x22/apps/panorama.png
/usr/share/icons/hicolor/22x22/apps/showfoto.png
/usr/share/icons/hicolor/256x256/apps/digikam.png
/usr/share/icons/hicolor/256x256/apps/showfoto.png
/usr/share/icons/hicolor/32x32/actions/albumfolder-importdir.png
/usr/share/icons/hicolor/32x32/actions/albumfolder-importimages.png
/usr/share/icons/hicolor/32x32/actions/albumfolder-new.png
/usr/share/icons/hicolor/32x32/actions/albumfolder-properties.png
/usr/share/icons/hicolor/32x32/actions/overexposure.png
/usr/share/icons/hicolor/32x32/actions/tag-addresbook.png
/usr/share/icons/hicolor/32x32/actions/tag-assigned.png
/usr/share/icons/hicolor/32x32/actions/tag-delete.png
/usr/share/icons/hicolor/32x32/actions/tag-events.png
/usr/share/icons/hicolor/32x32/actions/tag-folder.png
/usr/share/icons/hicolor/32x32/actions/tag-new.png
/usr/share/icons/hicolor/32x32/actions/tag-people.png
/usr/share/icons/hicolor/32x32/actions/tag-places.png
/usr/share/icons/hicolor/32x32/actions/tag-properties.png
/usr/share/icons/hicolor/32x32/actions/tag-recents.png
/usr/share/icons/hicolor/32x32/actions/tag-reset.png
/usr/share/icons/hicolor/32x32/actions/tag.png
/usr/share/icons/hicolor/32x32/actions/underexposure.png
/usr/share/icons/hicolor/32x32/apps/digikam.png
/usr/share/icons/hicolor/32x32/apps/dk-box.png
/usr/share/icons/hicolor/32x32/apps/dk-dropbox.png
/usr/share/icons/hicolor/32x32/apps/dk-facebook-white.png
/usr/share/icons/hicolor/32x32/apps/dk-facebook.png
/usr/share/icons/hicolor/32x32/apps/dk-flickr.png
/usr/share/icons/hicolor/32x32/apps/dk-googledrive.png
/usr/share/icons/hicolor/32x32/apps/dk-googlephoto.png
/usr/share/icons/hicolor/32x32/apps/dk-imageshack.png
/usr/share/icons/hicolor/32x32/apps/dk-imgur.png
/usr/share/icons/hicolor/32x32/apps/dk-ipfs.png
/usr/share/icons/hicolor/32x32/apps/dk-mediawiki.png
/usr/share/icons/hicolor/32x32/apps/dk-onedrive.png
/usr/share/icons/hicolor/32x32/apps/dk-pinterest.png
/usr/share/icons/hicolor/32x32/apps/dk-piwigo.png
/usr/share/icons/hicolor/32x32/apps/dk-rajce.png
/usr/share/icons/hicolor/32x32/apps/dk-smugmug.png
/usr/share/icons/hicolor/32x32/apps/expoblending.png
/usr/share/icons/hicolor/32x32/apps/panorama.png
/usr/share/icons/hicolor/32x32/apps/showfoto.png
/usr/share/icons/hicolor/48x48/apps/digikam.png
/usr/share/icons/hicolor/48x48/apps/dk-box.png
/usr/share/icons/hicolor/48x48/apps/dk-dropbox.png
/usr/share/icons/hicolor/48x48/apps/dk-facebook-white.png
/usr/share/icons/hicolor/48x48/apps/dk-facebook.png
/usr/share/icons/hicolor/48x48/apps/dk-flickr.png
/usr/share/icons/hicolor/48x48/apps/dk-googledrive.png
/usr/share/icons/hicolor/48x48/apps/dk-googlephoto.png
/usr/share/icons/hicolor/48x48/apps/dk-imageshack.png
/usr/share/icons/hicolor/48x48/apps/dk-imgur.png
/usr/share/icons/hicolor/48x48/apps/dk-ipfs.png
/usr/share/icons/hicolor/48x48/apps/dk-mediawiki.png
/usr/share/icons/hicolor/48x48/apps/dk-onedrive.png
/usr/share/icons/hicolor/48x48/apps/dk-pinterest.png
/usr/share/icons/hicolor/48x48/apps/dk-piwigo.png
/usr/share/icons/hicolor/48x48/apps/dk-rajce.png
/usr/share/icons/hicolor/48x48/apps/dk-smugmug.png
/usr/share/icons/hicolor/48x48/apps/expoblending.png
/usr/share/icons/hicolor/48x48/apps/panorama.png
/usr/share/icons/hicolor/48x48/apps/showfoto.png
/usr/share/icons/hicolor/64x64/apps/digikam.png
/usr/share/icons/hicolor/64x64/apps/showfoto.png
/usr/share/icons/hicolor/96x96/apps/expoblending.png
/usr/share/icons/hicolor/96x96/apps/panorama.png
/usr/share/icons/hicolor/scalable/apps/digikam.svgz
/usr/share/icons/hicolor/scalable/apps/dk-facebook-white.svgz
/usr/share/icons/hicolor/scalable/apps/dk-facebook.svgz
/usr/share/icons/hicolor/scalable/apps/dk-flickr.svgz
/usr/share/icons/hicolor/scalable/apps/dk-googlephoto.svgz
/usr/share/icons/hicolor/scalable/apps/dk-imgur.svgz
/usr/share/icons/hicolor/scalable/apps/dk-ipfs.svgz
/usr/share/icons/hicolor/scalable/apps/dk-mediawiki.svgz
/usr/share/icons/hicolor/scalable/apps/dk-piwigo.svgz
/usr/share/icons/hicolor/scalable/apps/dk-smugmug.svgz
/usr/share/icons/hicolor/scalable/apps/panorama.svgz
/usr/share/icons/hicolor/scalable/apps/showfoto.svgz
/usr/share/knotifications5/digikam.notifyrc
/usr/share/kxmlgui5/digikam/digikamui5.rc
/usr/share/kxmlgui5/digikam/imageeditorui5.rc
/usr/share/kxmlgui5/digikam/importui5.rc
/usr/share/kxmlgui5/digikam/lighttablewindowui5.rc
/usr/share/kxmlgui5/digikam/queuemgrwindowui5.rc
/usr/share/kxmlgui5/showfoto/showfotoui5.rc
/usr/share/metainfo/org.kde.digikam.appdata.xml
/usr/share/metainfo/org.kde.showfoto.appdata.xml
/usr/share/showfoto/data/banner-showfoto.png
/usr/share/showfoto/data/logo-showfoto.png
/usr/share/showfoto/data/splash-showfoto.png
/usr/share/solid/actions/digikam-opencamera.desktop

%files dev
%defattr(-,root,root,-)
/usr/lib64/haswell/libdigikamcore.so
/usr/lib64/haswell/libdigikamdatabase.so
/usr/lib64/haswell/libdigikamgui.so
/usr/lib64/libdigikamcore.so
/usr/lib64/libdigikamdatabase.so
/usr/lib64/libdigikamgui.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libdigikamcore.so.6.0.0
/usr/lib64/haswell/libdigikamdatabase.so.6.0.0
/usr/lib64/haswell/libdigikamgui.so.6.0.0
/usr/lib64/libdigikamcore.so.6.0.0
/usr/lib64/libdigikamdatabase.so.6.0.0
/usr/lib64/libdigikamgui.so.6.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/digikam/COPYING
/usr/share/package-licenses/digikam/COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/digikam/COPYING.LIB
/usr/share/package-licenses/digikam/core_libs_dimg_filters_greycstoration_cimg_LICENSE.txt
/usr/share/package-licenses/digikam/core_libs_rawengine_libraw_COPYRIGHT
/usr/share/package-licenses/digikam/core_libs_rawengine_libraw_LICENSE.CDDL
/usr/share/package-licenses/digikam/core_libs_rawengine_libraw_LICENSE.LGPL
/usr/share/package-licenses/digikam/core_tests_modeltest_LICENSE.GPL
/usr/share/package-licenses/digikam/core_utilities_assistants_webservices_common_o2_LICENSE
/usr/share/package-licenses/digikam/core_utilities_mediaserver_upnpsdk_Platinum_LICENSE.txt
/usr/share/package-licenses/digikam/project_bundles_macports_installer_GPL.txt
/usr/share/package-licenses/digikam/project_bundles_mxe_installer_GPL.txt

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cleanup_digikamdb.1
/usr/share/man/man1/digitaglinktree.1
