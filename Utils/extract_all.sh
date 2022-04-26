
echo "Create s1"

mkdir s1
for file in ./ROIs*_s1.tar.gz 
do
    mkdir tmp_tiles
    tar -xf $file -C tmp_tiles
    for ff in tmp_tiles/*/*/*.tif
    do
        mv $ff s1/
    done
    rm -r tmp_tiles
done
for f in s1/*.tif; do mv "$f" $(echo "$f" | sed 's/_s1//g'); done

echo "Create s2"

mkdir s2_cloudFree
for file in ./ROIs*_s2.tar.gz 
do
    mkdir tmp_tiles
    tar -xf $file -C tmp_tiles
    for ff in tmp_tiles/*/*/*.tif
    do
        mv $ff s2_cloudFree/
    done
    rm -r tmp_tiles
done
for f in s2_cloudFree/*.tif; do mv "$f" $(echo "$f" | sed 's/_s2//g'); done

echo "Create s2_cloudy"

mkdir s2_cloudy
for file in ./ROIs*_s2_cloudy.tar.gz 
do
    mkdir tmp_tiles
    tar -xf $file -C tmp_tiles
    for ff in tmp_tiles/*/*/*.tif
    do
        mv $ff s2_cloudy/
    done
    rm -r tmp_tiles
done
for f in s2_cloudy/*.tif; do mv "$f" $(echo "$f" | sed 's/_s2_cloudy//g'); done
