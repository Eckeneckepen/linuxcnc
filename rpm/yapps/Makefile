 DISTFILE = yapps2-2.2.1.tar.gz

target/bin/yapps2: dist/${DISTFILE}
	pip install dist/${DISTFILE} --prefix target

dist/${DISTFILE}: src/setup.py
	cd src && python3 setup.py sdist -d ../dist

src/setup.py:
	git clone https://github.com/smurfix/yapps src

.PHONY: clean distclean

clean:
	rm -rf dist
	rm -rf Yapps2.egg-info
	rm -rf target

distclean: clean
	rm -rf src
