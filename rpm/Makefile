
DESTDIR ?= ${CURDIR}/target

.PHONY: all clean

rpm:
	rpmbuild  --build-in-place --noclean --buildroot ${DESTDIR} \
		--define "_topdir ${CURDIR}" \
		--define "_builddir %{_topdir}" \
		--define "_rpmdir %{_topdir}" \
		--define "_sourcedir %{_topdir}/../src" \
		--define "_specdir %{_topdir}" \
		--define "_srcrpmdir %{_topdir}" \
		--define "_unpackaged_files_terminate_build 0" \
		--define "_missing_doc_files_terminate_build 0" \
		--define "_rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm" \
		--define "packager `whoami`" \
		-bb linuxcnc.spec

rip:
	make -C yapps
	export PATH=$$PATH:${CURDIR}/yapps/target/bin; \
	export PYTHONPATH=${CURDIR}/yapps/target/lib64/python3.11/site-packages; \
	export LDFLAGS="-ltirpc -lstdc++"; \
	cd ../src; \
	./autogen.sh; \
	./configure --with-realtime=uspace --enable-non-distributable=yes; \
	make -j 2; \
	make install DESTDIR=${CURDIR}/target

clean:
	rm -rf linuxcnc-2.9.3++-1.x86_64.rpm
	rm -rf target
