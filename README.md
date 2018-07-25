# Image filtering

im_filter.py - the main script that will take care of everything
has a detailed help section. Accessible via python im_filter.py --help 

Also for full usage, use:
```bash
./im_filter "./a.out" logoTemp.jpg
```

ToDo: Implement level functionality !

## building binaries

```bash
    sudo docker run --rm -it -v "$PWD":/usr/src/myapp -w /usr/src/myapp golang bash
    ./build.sh ./mat_to_img/
    ./build.sh ./img_to_mat/
```