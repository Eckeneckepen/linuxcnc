
 DESTDIR ?= ${CURDIR}/target
  SRCDIR  = ${CURDIR}/../src

.PHONY: rpm clean distclean

rpm:
	rpmbuild  --build-in-place --noclean --buildroot ${DESTDIR} \
		--define "_topdir ${CURDIR}" \
		--define "_builddir %{_topdir}" \
		--define "_buildrootdir %{buildroot}" \
		--define "_rpmdir %{_topdir}" \
		--define "_sourcedir ${SRCDIR}" \
		--define "_specdir %{_topdir}" \
		--define "_srcrpmdir %{_topdir}" \
		--define "_unpackaged_files_terminate_build 0" \
		--define "_missing_doc_files_terminate_build 0" \
		--define "_rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm" \
		--define "packager `whoami`" \
		-bb linuxcnc.spec

clean:
	rm -rf linuxcnc-2.9.3++-1.x86_64.rpm
	rm -rf ${DESTDIR}
	make -C yapps clean
	make -C ${SRCDIR} clean

distclean: clean
	make -C yapps distclean
	make -C ${SRCDIR} distclean
