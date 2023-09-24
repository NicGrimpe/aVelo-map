let
  pkgs = import <mypkgs> {};

  pythonWithPkgs = pkgs.python311.withPackages (pythonPkgs: with pythonPkgs; [
    # This list contains tools for Python development.
    # You can also add other tools, like black.
    #
    # Note that even if you add Python packages here like PyTorch or Tensorflow,
    # they will be reinstalled when running `pip -r requirements.txt` because
    # virtualenv is used below in the shellHook.
    ipython
    pip
    setuptools
    virtualenvwrapper
    wheel

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
