let
  pkgs = import <mypkgs> {};

  pythonWithPkgs = pkgs.python311.withPackages (pythonPkgs: with pythonPkgs; [
    folium
    contextily
    matplotlib
    tkinter
    geopandas
  ]);

  lib-path = with pkgs; lib.makeLibraryPath [
 #   libffi
  #  openssl
    stdenv.cc.cc
    zlib
    glibc
    # If you want to use CUDA, you should uncomment this line.
    # linuxPackages.nvidia_x11
  ];
in 

pkgs.mkShell {
  buildInputs = [
      # my python and packages
      pythonWithPkgs
      
      pkgs.black
      # other packages needed for compiling python libs
      #pkgs.readline
      #pkgs.libffi
      #pkgs.openssl
      #pkgs.zlib
      #pkgs.glibc
      #pkgs.stdenv.cc.cc.lib

      # unfortunately needed because of messing with LD_LIBRARY_PATH below
      #pkgs.git
      #pkgs.openssh
      #pkgs.rsync
    ];

    shellHook = ''
      # Allow the use of wheels.
      SOURCE_DATE_EPOCH=$(date +%s)
      # Augment the dynamic linker path
      #export "LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${lib-path}"
      # Setup the virtual environment if it doesn't already exist.
      export PYTHONPATH=`pwd`/$VENV/${pkgs.python311.sitePackages}/:$PYTHONPATH
    '';
}
