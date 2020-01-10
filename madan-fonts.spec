%global fontname madan
%global fontconf 65-0-%{fontname}.conf

Name: %{fontname}-fonts
Version: 2.000
Release: 10%{?dist}
Summary: Font for Nepali language
Group: User Interface/X
License: GPL+
URL: http://madanpuraskar.org/
# Found new following working Source URL. Use wget to download this archive
Source0: http://download.com.np/uploads/nepali_unicode/madan.zip
Source1: %{name}-fontconfig.conf
Source2: ttf2sfd.pe
Source3: sfd2ttf.pe
BuildArch: noarch
BuildRequires: fontforge
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem
# This patch will make sure "fc-scan madan.ttf |grep lang:" will show ne
Patch0: madan-fonts-2.000-bug842965-u0970.patch

%description
This package provides the Madan font for Nepali made by the
Madan Puraskar Pustakalaya project.

%prep
%setup -c -q
for file in madan/license.txt; do
 sed "s|\r||g" $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done

cp -p %{SOURCE2} %{SOURCE3} .

chmod 755 ttf2sfd.pe sfd2ttf.pe
./ttf2sfd.pe madan/*.ttf
rm -rf madan/*ttf
%patch0 -p1 -b .added-u0970-character
./sfd2ttf.pe madan/*.sfd


%build
echo "Nothing to do in Build."

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{fontname}/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.ttf
%doc %{fontname}/license.txt


%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.000-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Parag <pnemade AT redhat DOT com> - 2.000-9
- Resolves:rh#880037 - Update Source URL in spec file

* Fri Aug 03 2012 Parag <pnemade AT redhat DOT com> - 2.000-8
- Resolves: rh#842965, added character u0970
- Enabled autohint in fontconf file

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Parag <pnemade AT redhat DOT com> - 2.000-5
- Rebuild for rh#757105 - no font(:lang=blahblah) generated for Provides

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 18 2010 Parag <pnemade AT redhat.com> - 2.000-3
- Resolves: rh#586765 - Rename 65-madan.conf to 65-0-madan.conf    

* Tue Apr 20 2010 Parag <pnemade AT redhat.com> - 2.000-2
- Resolves: rh#578041-lang-specific overrides rule doesn't work as expected

* Tue Feb 23 2010 Parag <pnemade AT redhat.com> - 2.000-1
- Update to next upstream release
- Resolves: rh#335851-[ne_NP] Add license text file to madan-fonts package
- Resolves: rh#520047-[ne_NP] Need fontconfig rules for Madan font

* Tue Aug 11 2009 Parag <pnemade@redhat.com> - 1.0-11
- Fix source audit 2009-08-10

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Pravin Satpute <psatpute@redhat.com> - 1.0-9
- updated spec as per new packaging guideline

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-7
- fix license tag

* Mon Oct 15 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.0-6.fc8
- Spec update as per review

* Thu Oct 11 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.0-5.fc8
- Spec update as per reveiw

* Wed Sep 26 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.0-4.fc8
- Spec update as per review

* Fri Sep 21 2007 Rahul Bhalerao <rbahlera@redhat.com> - 1.0-3.fc8
- Added LICENSE as Source1

* Thu Sep 20 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.0-2.fc8
- Removed use of tarball and ghost files

* Thu Sep 13 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.0-1.fc8
- Initial packaging
