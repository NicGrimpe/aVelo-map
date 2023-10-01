let
  pkgs = import <nixpkgs> {};

  pythonWithPkgs = pkgs.python311.withPackages (pythonPkgs: with pythonPkgs; [
    folium
    geojson
  ]);
in 

pkgs.mkShell {
  buildInputs = [
      # my python and packages
      pythonWithPkgs
      
      pkgs.black
    ];

    shellHook = ''
      export PYTHONPATH=`pwd`/$VENV/${pkgs.python311.sitePackages}/:$PYTHONPATH
    '';
}
