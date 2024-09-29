#!/bin/bash
##
#

DESTDIR=${DESTDIR:-$PWD/target}

rpmbuild --buildroot=${DESTDIR} \
    --define "_topdir `pwd`" \
    --define "_builddir %{_topdir}" \
    --define "_rpmdir %{_topdir}" \
    --define "_sourcedir %{_topdir}/../src" \
    --define "_specdir %{_topdir}" \
    --define "_srcrpmdir %{_topdir}" \
    --define "_unpackaged_files_terminate_build 0" \
    --define "_missing_doc_files_terminate_build 0" \
    --define "_rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm" \
    -ba linuxcnc.spec
