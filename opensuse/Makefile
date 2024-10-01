
DESTDIR ?= ${CURDIR}/target

all:
	rpmbuild  --buildroot ${DESTDIR} \
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
		-vv -bb linuxcnc.spec
