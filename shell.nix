let
  pkgs = import <nixpkgs> {};

  pythonWithPkgs = pkgs.python311.withPackages (pythonPkgs: with pythonPkgs; [
    folium
    geojson
    requests
    beautifulsoup4
]);
in 

pkgs.mkShell {
  buildInputs = [
      pythonWithPkgs
      pkgs.black
    ];

    shellHook = ''
      export PYTHONPATH=`pwd`/$VENV/${pkgs.python311.sitePackages}/:$PYTHONPATH
    '';
}
