# Make sure to set configuration, needs to be before any galpy imports
from galpy.util import config
config.__config__.set('astropy','astropy-units','True')
import numpy
from astropy import units

def test_orbit_setup_radec_basic():
    from galpy.orbit import Orbit
    o= Orbit([10.*units.deg,-20.*units.deg,3.*units.kpc,
              -3.*units.mas/units.yr,2.*units.mas/units.yr,
              130.*units.km/units.s],radec=True)
    assert numpy.fabs(o.ra(use_physical=False)-10.) < 10.**-8., 'Orbit initialization with RA as Quantity does not work as expected'
    assert numpy.fabs(o.dec(use_physical=False)+20.) < 10.**-8., 'Orbit initialization with Dec as Quantity does not work as expected'
    assert numpy.fabs(o.dist(use_physical=False)-3.) < 10.**-8., 'Orbit initialization with distance as Quantity does not work as expected'
    assert numpy.fabs(o.pmra(use_physical=False)+3.) < 10.**-8., 'Orbit initialization with pmra as Quantity does not work as expected'
    assert numpy.fabs(o.pmdec(use_physical=False)-2.) < 10.**-8., 'Orbit initialization with pmdec as Quantity does not work as expected'
    assert numpy.fabs(o.vlos(use_physical=False)-130.) < 10.**-8., 'Orbit initialization with vlos as Quantity does not work as expected'
    return None

def test_orbit_setup_radec_oddunits():
    from galpy.orbit import Orbit
    o= Orbit([1.*units.rad,-0.25*units.rad,3000.*units.lyr,
              -3.*units.mas/units.s,2.*units.mas/units.kyr,
              130.*units.pc/units.Myr],radec=True)
    assert numpy.fabs(o.ra(use_physical=False)-1./numpy.pi*180.) < 10.**-8., 'Orbit initialization with RA as Quantity does not work as expected'
    assert numpy.fabs(o.dec(use_physical=False)+.25/numpy.pi*180.) < 10.**-8., 'Orbit initialization with Dec as Quantity does not work as expected'
    assert numpy.fabs(o.dist(use_physical=False)-3./3.26156) < 10.**-5., 'Orbit initialization with distance as Quantity does not work as expected'
    assert numpy.fabs((o.pmra(use_physical=False)+3.*units.yr.to(units.s))/o.pmra(use_physical=False)) < 10.**-8., 'Orbit initialization with pmra as Quantity does not work as expected'
    assert numpy.fabs((o.pmdec(use_physical=False)-2./10.**3.)/o.pmdec(use_physical=False)) < 10.**-4., 'Orbit initialization with pmdec as Quantity does not work as expected'
    assert numpy.fabs(o.vlos(use_physical=False)-130./1.0227121655399913) < 10.**-5., 'Orbit initialization with vlos as Quantity does not work as expected'
    return None

def test_orbit_setup_radec_uvw():
    from galpy.orbit import Orbit
    o= Orbit([1.*units.rad,-0.25*units.rad,3000.*units.pc,
              -30.*units.km/units.s,20.*units.km/units.s,
              130.*units.km/units.s],radec=True,uvw=True)
    assert numpy.fabs(o.ra(use_physical=False)-1./numpy.pi*180.) < 10.**-8., 'Orbit initialization with RA as Quantity does not work as expected'
    assert numpy.fabs(o.dec(use_physical=False)+.25/numpy.pi*180.) < 10.**-8., 'Orbit initialization with Dec as Quantity does not work as expected'
    assert numpy.fabs(o.dist(use_physical=False)-3.) < 10.**-8., 'Orbit initialization with distance as Quantity does not work as expected'
    assert numpy.fabs(o.U(use_physical=False)+30.) < 10.**-8., 'Orbit initialization with U as Quantity does not work as expected'
    assert numpy.fabs(o.V(use_physical=False)-20.) < 10.**-8., 'Orbit initialization with V as Quantity does not work as expected'
    assert numpy.fabs(o.W(use_physical=False)-130.) < 10.**-8., 'Orbit initialization with W as Quantity does not work as expected'
    return None

def test_orbit_setup_radec_uvw_oddunits():
    from galpy.orbit import Orbit
    o= Orbit([1.*units.rad,-0.25*units.rad,3000.*units.pc,
              -30.*units.pc/units.Myr,20.*units.pc/units.Myr,
              130.*units.pc/units.Myr],radec=True,uvw=True)
    assert numpy.fabs(o.ra(use_physical=False)-1./numpy.pi*180.) < 10.**-8., 'Orbit initialization with RA as Quantity does not work as expected'
    assert numpy.fabs(o.dec(use_physical=False)+.25/numpy.pi*180.) < 10.**-8., 'Orbit initialization with Dec as Quantity does not work as expected'
    assert numpy.fabs(o.dist(use_physical=False)-3.) < 10.**-8., 'Orbit initialization with distance as Quantity does not work as expected'
    assert numpy.fabs(o.U(use_physical=False)+30./1.0227121655399913) < 10.**-5., 'Orbit initialization with U as Quantity does not work as expected'
    assert numpy.fabs(o.V(use_physical=False)-20./1.0227121655399913) < 10.**-5., 'Orbit initialization with V as Quantity does not work as expected'
    assert numpy.fabs(o.W(use_physical=False)-130./1.0227121655399913) < 10.**-5., 'Orbit initialization with W as Quantity does not work as expected'
    return None

def test_orbit_setup_lb_basic():
    from galpy.orbit import Orbit
    o= Orbit([10.*units.deg,-20.*units.deg,3.*units.kpc,
              -3.*units.mas/units.yr,2.*units.mas/units.yr,
              130.*units.km/units.s],lb=True)
    assert numpy.fabs(o.ll(use_physical=False)-10.) < 10.**-8., 'Orbit initialization with ll as Quantity does not work as expected'
    assert numpy.fabs(o.bb(use_physical=False)+20.) < 10.**-8., 'Orbit initialization with bb as Quantity does not work as expected'
    assert numpy.fabs(o.dist(use_physical=False)-3.) < 10.**-8., 'Orbit initialization with distance as Quantity does not work as expected'
    assert numpy.fabs(o.pmll(use_physical=False)+3.) < 10.**-8., 'Orbit initialization with pmra as Quantity does not work as expected'
    assert numpy.fabs(o.pmbb(use_physical=False)-2.) < 10.**-8., 'Orbit initialization with pmdec as Quantity does not work as expected'
    assert numpy.fabs(o.vlos(use_physical=False)-130.) < 10.**-8., 'Orbit initialization with vlos as Quantity does not work as expected'
    return None

def test_orbit_setup_lb_oddunits():
    from galpy.orbit import Orbit
    o= Orbit([1.*units.rad,-0.25*units.rad,3000.*units.lyr,
              -3.*units.mas/units.s,2.*units.mas/units.kyr,
              130.*units.pc/units.Myr],lb=True)
    assert numpy.fabs(o.ll(use_physical=False)-1./numpy.pi*180.) < 10.**-8., 'Orbit initialization with ll as Quantity does not work as expected'
    assert numpy.fabs(o.bb(use_physical=False)+.25/numpy.pi*180.) < 10.**-8., 'Orbit initialization with bb as Quantity does not work as expected'
    assert numpy.fabs(o.dist(use_physical=False)-3./3.26156) < 10.**-5., 'Orbit initialization with distance as Quantity does not work as expected'
    assert numpy.fabs((o.pmll(use_physical=False)+3.*units.yr.to(units.s))/o.pmll(use_physical=False)) < 10.**-8., 'Orbit initialization with pmll as Quantity does not work as expected'
    assert numpy.fabs((o.pmbb(use_physical=False)-2./10.**3.)/o.pmbb(use_physical=False)) < 10.**-4., 'Orbit initialization with pmbb as Quantity does not work as expected'
    assert numpy.fabs(o.vlos(use_physical=False)-130./1.0227121655399913) < 10.**-5., 'Orbit initialization with vlos as Quantity does not work as expected'
    return None

def test_orbit_setup_lb_uvw():
    from galpy.orbit import Orbit
    o= Orbit([1.*units.rad,-0.25*units.rad,3000.*units.pc,
              -30.*units.km/units.s,20.*units.km/units.s,
              130.*units.km/units.s],lb=True,uvw=True)
    assert numpy.fabs(o.ll(use_physical=False)-1./numpy.pi*180.) < 10.**-8., 'Orbit initialization with ll as Quantity does not work as expected'
    assert numpy.fabs(o.bb(use_physical=False)+.25/numpy.pi*180.) < 10.**-8., 'Orbit initialization with bb as Quantity does not work as expected'
    assert numpy.fabs(o.dist(use_physical=False)-3.) < 10.**-8., 'Orbit initialization with distance as Quantity does not work as expected'
    assert numpy.fabs(o.U(use_physical=False)+30.) < 10.**-8., 'Orbit initialization with pmll as Quantity does not work as expected'
    assert numpy.fabs(o.V(use_physical=False)-20.) < 10.**-8., 'Orbit initialization with pmbb as Quantity does not work as expected'
    assert numpy.fabs(o.W(use_physical=False)-130.) < 10.**-8., 'Orbit initialization with W as Quantity does not work as expected'
    return None

def test_orbit_setup_lb_uvw_oddunits():
    from galpy.orbit import Orbit
    o= Orbit([1.*units.rad,-0.25*units.rad,3000.*units.pc,
              -30.*units.pc/units.Myr,20.*units.pc/units.Myr,
              130.*units.pc/units.Myr],lb=True,uvw=True)
    assert numpy.fabs(o.ll(use_physical=False)-1./numpy.pi*180.) < 10.**-8., 'Orbit initialization with ll as Quantity does not work as expected'
    assert numpy.fabs(o.bb(use_physical=False)+.25/numpy.pi*180.) < 10.**-8., 'Orbit initialization with bb as Quantity does not work as expected'
    assert numpy.fabs(o.dist(use_physical=False)-3.) < 10.**-8., 'Orbit initialization with distance as Quantity does not work as expected'
    assert numpy.fabs(o.U(use_physical=False)+30./1.0227121655399913) < 10.**-5., 'Orbit initialization with U as Quantity does not work as expected'
    assert numpy.fabs(o.V(use_physical=False)-20./1.0227121655399913) < 10.**-5., 'Orbit initialization with V as Quantity does not work as expected'
    assert numpy.fabs(o.W(use_physical=False)-130./1.0227121655399913) < 10.**-5., 'Orbit initialization with W as Quantity does not work as expected'
    return None

def test_orbit_setup_vxvv_fullorbit():
    from galpy.orbit import Orbit
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              500.*units.pc,-12.*units.km/units.s,45.*units.deg])
    assert numpy.fabs(o.R(use_physical=False)*o._ro-10.) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for FullOrbit'
    assert numpy.fabs(o.vR(use_physical=False)*o._vo+20.) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for FullOrbit'
    assert numpy.fabs(o.vT(use_physical=False)*o._vo-210.) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for FullOrbit'
    assert numpy.fabs(o.z(use_physical=False)*o._ro-0.5) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for FullOrbit'
    assert numpy.fabs(o.vz(use_physical=False)*o._vo+12) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for FullOrbit'
    assert numpy.fabs(o.phi(use_physical=False)-45./180.*numpy.pi) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for FullOrbit'
    return None

def test_orbit_setup_vxvv_rzorbit():
    from galpy.orbit import Orbit
    o= Orbit([10000.*units.lyr,-20.*units.km/units.s,210.*units.km/units.s,
              500.*units.pc,-12.*units.pc/units.Myr])
    assert numpy.fabs(o.R(use_physical=False)*o._ro-10./3.26156) < 10.**-5., 'Orbit initialization with vxvv as Quantity does not work as expected for RZOrbit'
    assert numpy.fabs(o.vR(use_physical=False)*o._vo+20.) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for RZOrbit'
    assert numpy.fabs(o.vT(use_physical=False)*o._vo-210.) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for RZOrbit'
    assert numpy.fabs(o.z(use_physical=False)*o._ro-0.5) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for RZOrbit'
    assert numpy.fabs(o.vz(use_physical=False)*o._vo+12./1.0227121655399913) < 10.**-5., 'Orbit initialization with vxvv as Quantity does not work as expected for RZOrbit'
    return None

def test_orbit_setup_vxvv_planarorbit():
    from galpy.orbit import Orbit
    o= Orbit([10000.*units.lyr,-20.*units.km/units.s,210.*units.km/units.s,
              3.*units.rad])
    assert numpy.fabs(o.R(use_physical=False)*o._ro-10./3.26156) < 10.**-5., 'Orbit initialization with vxvv as Quantity does not work as expected for RZOrbit'
    assert numpy.fabs(o.vR(use_physical=False)*o._vo+20.) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for RZOrbit'
    assert numpy.fabs(o.vT(use_physical=False)*o._vo-210.) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for RZOrbit'
    assert numpy.fabs(o.phi(use_physical=False)-3.) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for FullOrbit'
    return None

def test_orbit_setup_vxvv_planarrorbit():
    from galpy.orbit import Orbit
    o= Orbit([7.*units.kpc,-2.*units.km/units.s,210.*units.km/units.s],
             ro=10.,vo=150.)
    assert numpy.fabs(o.R(use_physical=False)*o._ro-7.) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for RZOrbit'
    assert numpy.fabs(o.vR(use_physical=False)*o._vo+2.) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for RZOrbit'
    assert numpy.fabs(o.vT(use_physical=False)*o._vo-210.) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for RZOrbit'
    return None

def test_orbit_setup_vxvv_linearorbit():
    from galpy.orbit import Orbit
    o= Orbit([7.*units.kpc,-21.*units.pc/units.Myr])
    assert numpy.fabs(o.x(use_physical=False)*o._ro-7.) < 10.**-8., 'Orbit initialization with vxvv as Quantity does not work as expected for RZOrbit'
    assert numpy.fabs(o.vx(use_physical=False)*o._vo+21./1.0227121655399913) < 10.**-5., 'Orbit initialization with vxvv as Quantity does not work as expected for RZOrbit'
    return None

def test_orbit_setup_solarmotion():
    from galpy.orbit import Orbit
    o= Orbit([1.,0.1,1.1,0.2,0.1,0.],
             solarmotion=units.Quantity([13.,25.,8.],unit=units.km/units.s))
    assert numpy.fabs(o._orb._solarmotion[0]-13.) < 10.**-8., 'solarmotion in Orbit setup as Quantity does not work as expected'
    assert numpy.fabs(o._orb._solarmotion[1]-25.) < 10.**-8., 'solarmotion in Orbit setup as Quantity does not work as expected'
    assert numpy.fabs(o._orb._solarmotion[2]-8.) < 10.**-8., 'solarmotion in Orbit setup as Quantity does not work as expected'
    return None

def test_orbit_setup_solarmotion_oddunits():
    from galpy.orbit import Orbit
    o= Orbit([1.,0.1,1.1,0.2,0.1,0.],
             solarmotion=units.Quantity([13.,25.,8.],unit=units.kpc/units.Gyr))
    assert numpy.fabs(o._orb._solarmotion[0]-13./1.0227121655399913) < 10.**-5., 'solarmotion in Orbit setup as Quantity does not work as expected'
    assert numpy.fabs(o._orb._solarmotion[1]-25./1.0227121655399913) < 10.**-5., 'solarmotion in Orbit setup as Quantity does not work as expected'
    assert numpy.fabs(o._orb._solarmotion[2]-8./1.0227121655399913) < 10.**-5., 'solarmotion in Orbit setup as Quantity does not work as expected'
    return None

def test_orbit_setup_roAsQuantity():
    from galpy.orbit import Orbit
    o= Orbit([1.,0.1,1.1,0.2,0.1,0.],ro=11*units.kpc)
    assert numpy.fabs(o._ro-11.) < 10.**-10., 'ro in Orbit setup as Quantity does not work as expected'
    assert numpy.fabs(o._orb._ro-11.) < 10.**-10., 'ro in Orbit setup as Quantity does not work as expected'
    return None

def test_orbit_setup_roAsQuantity_oddunits():
    from galpy.orbit import Orbit
    o= Orbit([1.,0.1,1.1,0.2,0.1,0.],ro=11*units.lyr)
    assert numpy.fabs(o._ro-11.*units.lyr.to(units.kpc)) < 10.**-10., 'ro in Orbit setup as Quantity does not work as expected'
    assert numpy.fabs(o._orb._ro-11.*units.lyr.to(units.kpc)) < 10.**-10., 'ro in Orbit setup as Quantity does not work as expected'
    return None

def test_orbit_setup_voAsQuantity():
    from galpy.orbit import Orbit
    o= Orbit([1.,0.1,1.1,0.2,0.1,0.],vo=210*units.km/units.s)
    assert numpy.fabs(o._vo-210.) < 10.**-10., 'vo in Orbit setup as Quantity does not work as expected'
    assert numpy.fabs(o._orb._vo-210.) < 10.**-10., 'vo in Orbit setup as Quantity does not work as expected'
    return None

def test_orbit_setup_voAsQuantity_oddunits():
    from galpy.orbit import Orbit
    o= Orbit([1.,0.1,1.1,0.2,0.1,0.],vo=210*units.pc/units.Myr)
    assert numpy.fabs(o._vo-210.*(units.pc/units.Myr).to(units.km/units.s)) < 10.**-10., 'vo in Orbit setup as Quantity does not work as expected'
    assert numpy.fabs(o._orb._vo-210.*(units.pc/units.Myr).to(units.km/units.s)) < 10.**-10., 'vo in Orbit setup as Quantity does not work as expected'
    return None

def test_orbit_setup_zoAsQuantity():
    from galpy.orbit import Orbit
    o= Orbit([1.,0.1,1.1,0.2,0.1,0.],zo=12*units.pc)
    assert numpy.fabs(o._orb._zo-0.012) < 10.**-10., 'zo in Orbit setup as Quantity does not work as expected'
    return None

def test_orbit_setup_zoAsQuantity_oddunits():
    from galpy.orbit import Orbit
    o= Orbit([1.,0.1,1.1,0.2,0.1,0.],zo=13*units.lyr)
    assert numpy.fabs(o._orb._zo-13.*units.lyr.to(units.kpc)) < 10.**-10., 'zo in Orbit setup as Quantity does not work as expected'
    return None

def test_orbit_method_returntype_scalar():
    from galpy.orbit import Orbit
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              500.*units.pc,-12.*units.km/units.s,45.*units.deg])
    from galpy.potential import MWPotential2014
    assert isinstance(o.E(pot=MWPotential2014),units.Quantity), 'Orbit method E does not return Quantity when it should'
    assert isinstance(o.ER(pot=MWPotential2014),units.Quantity), 'Orbit method ER does not return Quantity when it should'
    assert isinstance(o.Ez(pot=MWPotential2014),units.Quantity), 'Orbit method Ez does not return Quantity when it should'
    assert isinstance(o.Jacobi(pot=MWPotential2014),units.Quantity), 'Orbit method Jacobi does not return Quantity when it should'
    assert isinstance(o.L(),units.Quantity), 'Orbit method L does not return Quantity when it should'
    assert isinstance(o.rap(pot=MWPotential2014,analytic=True),units.Quantity), 'Orbit method rap does not return Quantity when it should'
    assert isinstance(o.rperi(pot=MWPotential2014,analytic=True),units.Quantity), 'Orbit method rperi does not return Quantity when it should'
    assert isinstance(o.zmax(pot=MWPotential2014,analytic=True),units.Quantity), 'Orbit method zmax does not return Quantity when it should'
    assert isinstance(o.jr(pot=MWPotential2014,type='staeckel',delta=0.5),units.Quantity), 'Orbit method jr does not return Quantity when it should'
    assert isinstance(o.jp(pot=MWPotential2014,type='staeckel',delta=0.5),units.Quantity), 'Orbit method jp does not return Quantity when it should'
    assert isinstance(o.jz(pot=MWPotential2014,type='staeckel',delta=0.5),units.Quantity), 'Orbit method jz does not return Quantity when it should'
    assert isinstance(o.wr(pot=MWPotential2014,type='staeckel',delta=0.5),units.Quantity), 'Orbit method wr does not return Quantity when it should'
    assert isinstance(o.wp(pot=MWPotential2014,type='staeckel',delta=0.5),units.Quantity), 'Orbit method wp does not return Quantity when it should'
    assert isinstance(o.wz(pot=MWPotential2014,type='staeckel',delta=0.5),units.Quantity), 'Orbit method wz does not return Quantity when it should'
    assert isinstance(o.Tr(pot=MWPotential2014,type='staeckel',delta=0.5),units.Quantity), 'Orbit method Tr does not return Quantity when it should'
    assert isinstance(o.Tp(pot=MWPotential2014,type='staeckel',delta=0.5),units.Quantity), 'Orbit method Tp does not return Quantity when it should'
    assert isinstance(o.Tz(pot=MWPotential2014,type='staeckel',delta=0.5),units.Quantity), 'Orbit method Tz does not return Quantity when it should'
    assert isinstance(o.Or(pot=MWPotential2014,type='staeckel',delta=0.5),units.Quantity), 'Orbit method Or does not return Quantity when it should'
    assert isinstance(o.Op(pot=MWPotential2014,type='staeckel',delta=0.5),units.Quantity), 'Orbit method Op does not return Quantity when it should'
    assert isinstance(o.Oz(pot=MWPotential2014,type='staeckel',delta=0.5),units.Quantity), 'Orbit method Oz does not return Quantity when it should'
    assert isinstance(o.time(),units.Quantity), 'Orbit method time does not return Quantity when it should'
    assert isinstance(o.R(),units.Quantity), 'Orbit method R does not return Quantity when it should'
    assert isinstance(o.vR(),units.Quantity), 'Orbit method vR does not return Quantity when it should'
    assert isinstance(o.vT(),units.Quantity), 'Orbit method vT does not return Quantity when it should'
    assert isinstance(o.z(),units.Quantity), 'Orbit method z does not return Quantity when it should'
    assert isinstance(o.vz(),units.Quantity), 'Orbit method vz does not return Quantity when it should'
    assert isinstance(o.phi(),units.Quantity), 'Orbit method phi does not return Quantity when it should'
    assert isinstance(o.vphi(),units.Quantity), 'Orbit method vphi does not return Quantity when it should'
    assert isinstance(o.x(),units.Quantity), 'Orbit method x does not return Quantity when it should'
    assert isinstance(o.y(),units.Quantity), 'Orbit method y does not return Quantity when it should'
    assert isinstance(o.vx(),units.Quantity), 'Orbit method vx does not return Quantity when it should'
    assert isinstance(o.vy(),units.Quantity), 'Orbit method vy does not return Quantity when it should'
    assert isinstance(o.ra(),units.Quantity), 'Orbit method ra does not return Quantity when it should'
    assert isinstance(o.dec(),units.Quantity), 'Orbit method dec does not return Quantity when it should'
    assert isinstance(o.ll(),units.Quantity), 'Orbit method ll does not return Quantity when it should'
    assert isinstance(o.bb(),units.Quantity), 'Orbit method bb does not return Quantity when it should'
    assert isinstance(o.dist(),units.Quantity), 'Orbit method dist does not return Quantity when it should'
    assert isinstance(o.pmra(),units.Quantity), 'Orbit method pmra does not return Quantity when it should'
    assert isinstance(o.pmdec(),units.Quantity), 'Orbit method pmdec does not return Quantity when it should'
    assert isinstance(o.pmll(),units.Quantity), 'Orbit method pmll does not return Quantity when it should'
    assert isinstance(o.pmbb(),units.Quantity), 'Orbit method pmbb does not return Quantity when it should'
    assert isinstance(o.vlos(),units.Quantity), 'Orbit method vlos does not return Quantity when it should'
    assert isinstance(o.vra(),units.Quantity), 'Orbit method vra does not return Quantity when it should'
    assert isinstance(o.vdec(),units.Quantity), 'Orbit method vdec does not return Quantity when it should'
    assert isinstance(o.vll(),units.Quantity), 'Orbit method vll does not return Quantity when it should'
    assert isinstance(o.vbb(),units.Quantity), 'Orbit method vbb does not return Quantity when it should'
    assert isinstance(o.helioX(),units.Quantity), 'Orbit method helioX does not return Quantity when it should'
    assert isinstance(o.helioY(),units.Quantity), 'Orbit method helioY does not return Quantity when it should'
    assert isinstance(o.helioZ(),units.Quantity), 'Orbit method helioZ does not return Quantity when it should'
    assert isinstance(o.U(),units.Quantity), 'Orbit method U does not return Quantity when it should'
    assert isinstance(o.V(),units.Quantity), 'Orbit method V does not return Quantity when it should'
    assert isinstance(o.W(),units.Quantity), 'Orbit method W does not return Quantity when it should'
    return None

def test_orbit_method_returntype():
    from galpy.orbit import Orbit
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              500.*units.pc,-12.*units.km/units.s,45.*units.deg])
    from galpy.potential import MWPotential2014
    ts= numpy.linspace(0.,6.,1001)
    o.integrate(ts,MWPotential2014)
    assert isinstance(o.E(ts),units.Quantity), 'Orbit method E does not return Quantity when it should'
    assert isinstance(o.ER(ts),units.Quantity), 'Orbit method ER does not return Quantity when it should'
    assert isinstance(o.Ez(ts),units.Quantity), 'Orbit method Ez does not return Quantity when it should'
    assert isinstance(o.Jacobi(ts),units.Quantity), 'Orbit method Jacobi does not return Quantity when it should'
    assert isinstance(o.L(ts),units.Quantity), 'Orbit method L does not return Quantity when it should'
    assert isinstance(o.time(ts),units.Quantity), 'Orbit method time does not return Quantity when it should'
    assert isinstance(o.R(ts),units.Quantity), 'Orbit method R does not return Quantity when it should'
    assert isinstance(o.vR(ts),units.Quantity), 'Orbit method vR does not return Quantity when it should'
    assert isinstance(o.vT(ts),units.Quantity), 'Orbit method vT does not return Quantity when it should'
    assert isinstance(o.z(ts),units.Quantity), 'Orbit method z does not return Quantity when it should'
    assert isinstance(o.vz(ts),units.Quantity), 'Orbit method vz does not return Quantity when it should'
    assert isinstance(o.phi(ts),units.Quantity), 'Orbit method phi does not return Quantity when it should'
    assert isinstance(o.vphi(ts),units.Quantity), 'Orbit method vphi does not return Quantity when it should'
    assert isinstance(o.x(ts),units.Quantity), 'Orbit method x does not return Quantity when it should'
    assert isinstance(o.y(ts),units.Quantity), 'Orbit method y does not return Quantity when it should'
    assert isinstance(o.vx(ts),units.Quantity), 'Orbit method vx does not return Quantity when it should'
    assert isinstance(o.vy(ts),units.Quantity), 'Orbit method vy does not return Quantity when it should'
    assert isinstance(o.ra(ts),units.Quantity), 'Orbit method ra does not return Quantity when it should'
    assert isinstance(o.dec(ts),units.Quantity), 'Orbit method dec does not return Quantity when it should'
    assert isinstance(o.ll(ts),units.Quantity), 'Orbit method ll does not return Quantity when it should'
    assert isinstance(o.bb(ts),units.Quantity), 'Orbit method bb does not return Quantity when it should'
    assert isinstance(o.dist(ts),units.Quantity), 'Orbit method dist does not return Quantity when it should'
    assert isinstance(o.pmra(ts),units.Quantity), 'Orbit method pmra does not return Quantity when it should'
    assert isinstance(o.pmdec(ts),units.Quantity), 'Orbit method pmdec does not return Quantity when it should'
    assert isinstance(o.pmll(ts),units.Quantity), 'Orbit method pmll does not return Quantity when it should'
    assert isinstance(o.pmbb(ts),units.Quantity), 'Orbit method pmbb does not return Quantity when it should'
    assert isinstance(o.vlos(ts),units.Quantity), 'Orbit method vlos does not return Quantity when it should'
    assert isinstance(o.vra(ts),units.Quantity), 'Orbit method vra does not return Quantity when it should'
    assert isinstance(o.vdec(ts),units.Quantity), 'Orbit method vdec does not return Quantity when it should'
    assert isinstance(o.vll(ts),units.Quantity), 'Orbit method vll does not return Quantity when it should'
    assert isinstance(o.vbb(ts),units.Quantity), 'Orbit method vbb does not return Quantity when it should'
    assert isinstance(o.helioX(ts),units.Quantity), 'Orbit method helioX does not return Quantity when it should'
    assert isinstance(o.helioY(ts),units.Quantity), 'Orbit method helioY does not return Quantity when it should'
    assert isinstance(o.helioZ(ts),units.Quantity), 'Orbit method helioZ does not return Quantity when it should'
    assert isinstance(o.U(ts),units.Quantity), 'Orbit method U does not return Quantity when it should'
    assert isinstance(o.V(ts),units.Quantity), 'Orbit method V does not return Quantity when it should'
    assert isinstance(o.W(ts),units.Quantity), 'Orbit method W does not return Quantity when it should'
    return None

def test_orbit_method_returnunit():
    from galpy.orbit import Orbit
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              500.*units.pc,-12.*units.km/units.s,45.*units.deg])
    from galpy.potential import MWPotential2014
    try:
        o.E(pot=MWPotential2014).to(units.km**2/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Orbit method E does not return Quantity with the right units')
    try:
        o.ER(pot=MWPotential2014).to(units.km**2/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Orbit method ER does not return Quantity with the right units')
    try:
        o.Ez(pot=MWPotential2014).to(units.km**2/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Orbit method Ez does not return Quantity with the right units')
    try:
        o.Jacobi(pot=MWPotential2014).to(units.km**2/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Orbit method Jacobi does not return Quantity with the right units')
    try:
        o.L().to(units.km**2/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method L does not return Quantity with the right units')
    try:
        o.rap(pot=MWPotential2014,analytic=True).to(units.kpc)
    except units.UnitConversionError:
        raise AssertionError('Orbit method rap does not return Quantity with the right units')
    try:
        o.rperi(pot=MWPotential2014,analytic=True).to(units.kpc)
    except units.UnitConversionError:
        raise AssertionError('Orbit method rperi does not return Quantity with the right units')
    try:
        o.zmax(pot=MWPotential2014,analytic=True).to(units.kpc)
    except units.UnitConversionError:
        raise AssertionError('Orbit method zmax does not return Quantity with the right units')
    try:
        o.jr(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.km**2/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method jr does not return Quantity with the right units')
    try:
        o.jp(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.km**2/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method jp does not return Quantity with the right units')
    try:
        o.jz(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.km**2/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method jz does not return Quantity with the right units')
    try:
        o.wr(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.rad)
    except units.UnitConversionError:
        raise AssertionError('Orbit method wr does not return Quantity with the right units')
    try:
        o.wp(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.rad)
    except units.UnitConversionError:
        raise AssertionError('Orbit method wp does not return Quantity with the right units')
    try:
        o.wz(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.rad)
    except units.UnitConversionError:
        raise AssertionError('Orbit method wz does not return Quantity with the right units')
    try:
        o.Tr(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.yr)
    except units.UnitConversionError:
        raise AssertionError('Orbit method Tr does not return Quantity with the right units')
    try:
        o.Tp(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.yr)
    except units.UnitConversionError:
        raise AssertionError('Orbit method Tp does not return Quantity with the right units')
    try:
        o.Tz(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.yr)
    except units.UnitConversionError:
        raise AssertionError('Orbit method Tz does not return Quantity with the right units')
    try:
        o.Or(pot=MWPotential2014,type='staeckel',delta=0.5).to(1/units.yr)
    except units.UnitConversionError:
        raise AssertionError('Orbit method Or does not return Quantity with the right units')
    try:
        o.Op(pot=MWPotential2014,type='staeckel',delta=0.5).to(1/units.yr)
    except units.UnitConversionError:
        raise AssertionError('Orbit method Op does not return Quantity with the right units')
    try:
        o.Oz(pot=MWPotential2014,type='staeckel',delta=0.5).to(1/units.yr)
    except units.UnitConversionError:
        raise AssertionError('Orbit method Oz does not return Quantity with the right units')
    try:
        o.time().to(units.yr)
    except units.UnitConversionError:
        raise AssertionError('Orbit method time does not return Quantity with the right units')
    try:
        o.R().to(units.pc)
    except units.UnitConversionError:
        raise AssertionError('Orbit method R does not return Quantity with the right units')
    try:
        o.vR().to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method vR does not return Quantity with the right units')
    try:
        o.vT().to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method vT does not return Quantity with the right units')
    try:
        o.z().to(units.pc)
    except units.UnitConversionError:
        raise AssertionError('Orbit method z does not return Quantity with the right units')
    try:
        o.vz().to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method vz does not return Quantity with the right units')
    try:
        o.phi().to(units.deg)
    except units.UnitConversionError:
        raise AssertionError('Orbit method phi does not return Quantity with the right units')
    try:
        o.vphi().to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method vphi does not return Quantity with the right units')
    try:
        o.x().to(units.pc)
    except units.UnitConversionError:
        raise AssertionError('Orbit method x does not return Quantity with the right units')
    try:
        o.y().to(units.pc)
    except units.UnitConversionError:
        raise AssertionError('Orbit method y does not return Quantity with the right units')
    try:
        o.vx().to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method vx does not return Quantity with the right units')
    try:
        o.vy().to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method vy does not return Quantity with the right units')
    try:
        o.ra().to(units.rad)
    except units.UnitConversionError:
        raise AssertionError('Orbit method ra does not return Quantity with the right units')
    try:
        o.dec().to(units.rad)
    except units.UnitConversionError:
        raise AssertionError('Orbit method dec does not return Quantity with the right units')
    try:
        o.ll().to(units.rad)
    except units.UnitConversionError:
        raise AssertionError('Orbit method ll does not return Quantity with the right units')
    try:
        o.bb().to(units.rad)
    except units.UnitConversionError:
        raise AssertionError('Orbit method bb does not return Quantity with the right units')
    try:
        o.dist().to(units.kpc)
    except units.UnitConversionError:
        raise AssertionError('Orbit method dist does not return Quantity with the right units')
    try:
        o.pmra().to(units.mas/units.yr)
    except units.UnitConversionError:
        raise AssertionError('Orbit method pmra does not return Quantity with the right units')
    try:
        o.pmdec().to(units.mas/units.yr)
    except units.UnitConversionError:
        raise AssertionError('Orbit method pmdec does not return Quantity with the right units')
    try:
        o.pmll().to(units.mas/units.yr)
    except units.UnitConversionError:
        raise AssertionError('Orbit method pmll does not return Quantity with the right units')
    try:
        o.pmbb().to(units.mas/units.yr)
    except units.UnitConversionError:
        raise AssertionError('Orbit method pmbb does not return Quantity with the right units')
    try:
        o.vlos().to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method vlos does not return Quantity with the right units')
    try:
        o.vra().to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method vra does not return Quantity with the right units')
    try:
        o.vdec().to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method vdec does not return Quantity with the right units')
    try:
        o.vll().to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method vll does not return Quantity with the right units')
    try:
        o.vbb().to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method vbb does not return Quantity with the right units')
    try:
        o.helioX().to(units.pc)
    except units.UnitConversionError:
        raise AssertionError('Orbit method helioX does not return Quantity with the right units')
    try:
        o.helioY().to(units.pc)
    except units.UnitConversionError:
        raise AssertionError('Orbit method helioY does not return Quantity with the right units')
    try:
        o.helioZ().to(units.pc)
    except units.UnitConversionError:
        raise AssertionError('Orbit method helioZ does not return Quantity with the right units')
    try:
        o.U().to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method U does not return Quantity with the right units')
    try:
        o.V().to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method V does not return Quantity with the right units')
    try:
        o.W().to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Orbit method W does not return Quantity with the right units')
    return None

def test_orbit_method_value():
    from galpy.orbit import Orbit
    from galpy.potential import MWPotential2014
    from galpy.util import bovy_conversion
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              500.*units.pc,-12.*units.km/units.s,45.*units.deg])
    oc= o()
    oc.turn_physical_off()
    assert numpy.fabs(o.E(pot=MWPotential2014).to(units.km**2/units.s**2).value-oc.E(pot=MWPotential2014)*o._vo**2.) < 10.**-8., 'Orbit method E does not return the correct value as Quantity'
    assert numpy.fabs(o.ER(pot=MWPotential2014).to(units.km**2/units.s**2).value-oc.ER(pot=MWPotential2014)*o._vo**2.) < 10.**-8., 'Orbit method ER does not return the correct value as Quantity'
    assert numpy.fabs(o.Ez(pot=MWPotential2014).to(units.km**2/units.s**2).value-oc.Ez(pot=MWPotential2014)*o._vo**2.) < 10.**-8., 'Orbit method Ez does not return the correct value as Quantity'
    assert numpy.fabs(o.Jacobi(pot=MWPotential2014).to(units.km**2/units.s**2).value-oc.Jacobi(pot=MWPotential2014)*o._vo**2.) < 10.**-8., 'Orbit method Jacobi does not return the correct value as Quantity'
    assert numpy.all(numpy.fabs(o.L(pot=MWPotential2014).to(units.km/units.s*units.kpc).value-oc.L(pot=MWPotential2014)*o._ro*o._vo) < 10.**-8.), 'Orbit method L does not return the correct value as Quantity'
    assert numpy.fabs(o.rap(pot=MWPotential2014,analytic=True).to(units.kpc).value-oc.rap(pot=MWPotential2014,analytic=True)*o._ro) < 10.**-8., 'Orbit method rap does not return the correct value as Quantity'
    assert numpy.fabs(o.rperi(pot=MWPotential2014,analytic=True).to(units.kpc).value-oc.rperi(pot=MWPotential2014,analytic=True)*o._ro) < 10.**-8., 'Orbit method rperi does not return the correct value as Quantity'
    assert numpy.fabs(o.zmax(pot=MWPotential2014,analytic=True).to(units.kpc).value-oc.zmax(pot=MWPotential2014,analytic=True)*o._ro) < 10.**-8., 'Orbit method zmax does not return the correct value as Quantity'
    assert numpy.fabs(o.jr(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.km/units.s*units.kpc).value-oc.jr(pot=MWPotential2014,type='staeckel',delta=0.5)*o._ro*o._vo) < 10.**-8., 'Orbit method jr does not return the correct value as Quantity'
    assert numpy.fabs(o.jp(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.km/units.s*units.kpc).value-oc.jp(pot=MWPotential2014,type='staeckel',delta=0.5)*o._ro*o._vo) < 10.**-8., 'Orbit method jp does not return the correct value as Quantity'
    assert numpy.fabs(o.jz(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.km/units.s*units.kpc).value-oc.jz(pot=MWPotential2014,type='staeckel',delta=0.5)*o._ro*o._vo) < 10.**-8., 'Orbit method jz does not return the correct value as Quantity'
    assert numpy.fabs(o.wr(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.rad).value-oc.wr(pot=MWPotential2014,type='staeckel',delta=0.5)) < 10.**-8., 'Orbit method wr does not return the correct value as Quantity'
    assert numpy.fabs(o.wp(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.rad).value-oc.wp(pot=MWPotential2014,type='staeckel',delta=0.5)) < 10.**-8., 'Orbit method wp does not return the correct value as Quantity'
    assert numpy.fabs(o.wz(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.rad).value-oc.wz(pot=MWPotential2014,type='staeckel',delta=0.5)) < 10.**-8., 'Orbit method wz does not return the correct value as Quantity'
    assert numpy.fabs(o.Tr(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.Gyr).value-oc.Tr(pot=MWPotential2014,type='staeckel',delta=0.5)*bovy_conversion.time_in_Gyr(o._vo,o._ro)) < 10.**-8., 'Orbit method Tr does not return the correct value as Quantity'
    assert numpy.fabs(o.Tp(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.Gyr).value-oc.Tp(pot=MWPotential2014,type='staeckel',delta=0.5)*bovy_conversion.time_in_Gyr(o._vo,o._ro)) < 10.**-8., 'Orbit method Tp does not return the correct value as Quantity'
    assert numpy.fabs(o.Tz(pot=MWPotential2014,type='staeckel',delta=0.5).to(units.Gyr).value-oc.Tz(pot=MWPotential2014,type='staeckel',delta=0.5)*bovy_conversion.time_in_Gyr(o._vo,o._ro)) < 10.**-8., 'Orbit method Tz does not return the correct value as Quantity'
    assert numpy.fabs(o.Or(pot=MWPotential2014,type='staeckel',delta=0.5).to(1/units.Gyr).value-oc.Or(pot=MWPotential2014,type='staeckel',delta=0.5)*bovy_conversion.freq_in_Gyr(o._vo,o._ro)) < 10.**-8., 'Orbit method Or does not return the correct value as Quantity'
    assert numpy.fabs(o.Op(pot=MWPotential2014,type='staeckel',delta=0.5).to(1/units.Gyr).value-oc.Op(pot=MWPotential2014,type='staeckel',delta=0.5)*bovy_conversion.freq_in_Gyr(o._vo,o._ro)) < 10.**-8., 'Opbit method Or does not return the correct value as Quantity'
    assert numpy.fabs(o.Oz(pot=MWPotential2014,type='staeckel',delta=0.5).to(1/units.Gyr).value-oc.Oz(pot=MWPotential2014,type='staeckel',delta=0.5)*bovy_conversion.freq_in_Gyr(o._vo,o._ro)) < 10.**-8., 'Ozbit method Or does not return the correct value as Quantity'
    assert numpy.fabs(o.time().to(units.Gyr).value-oc.time()*bovy_conversion.time_in_Gyr(o._vo,o._ro)) < 10.**-8., 'Orbit method time does not return the correct value as Quantity'
    assert numpy.fabs(o.R().to(units.kpc).value-oc.R()*o._ro) < 10.**-8., 'Orbit method R does not return the correct value as Quantity'
    assert numpy.fabs(o.vR().to(units.km/units.s).value-oc.vR()*o._vo) < 10.**-8., 'Orbit method vR does not return the correct value as Quantity'
    assert numpy.fabs(o.vT().to(units.km/units.s).value-oc.vT()*o._vo) < 10.**-8., 'Orbit method vT does not return the correct value as Quantity'
    assert numpy.fabs(o.z().to(units.kpc).value-oc.z()*o._ro) < 10.**-8., 'Orbit method z does not return the correct value as Quantity'
    assert numpy.fabs(o.vz().to(units.km/units.s).value-oc.vz()*o._vo) < 10.**-8., 'Orbit method vz does not return the correct value as Quantity'
    assert numpy.fabs(o.phi().to(units.rad).value-oc.phi()) < 10.**-8., 'Orbit method phi does not return the correct value as Quantity'
    assert numpy.fabs(o.vphi().to(units.km/units.s).value-oc.vphi()*o._vo) < 10.**-8., 'Orbit method vphi does not return the correct value as Quantity'
    assert numpy.fabs(o.x().to(units.kpc).value-oc.x()*o._ro) < 10.**-8., 'Orbit method x does not return the correct value as Quantity'
    assert numpy.fabs(o.y().to(units.kpc).value-oc.y()*o._ro) < 10.**-8., 'Orbit method y does not return the correct value as Quantity'
    assert numpy.fabs(o.vx().to(units.km/units.s).value-oc.vx()*o._vo) < 10.**-8., 'Orbit method vx does not return the correct value as Quantity'
    assert numpy.fabs(o.vy().to(units.km/units.s).value-oc.vy()*o._vo) < 10.**-8., 'Orbit method vy does not return the correct value as Quantity'
    assert numpy.fabs(o.ra().to(units.deg).value-oc.ra()) < 10.**-8., 'Orbit method ra does not return the correct value as Quantity'
    assert numpy.fabs(o.dec().to(units.deg).value-oc.dec()) < 10.**-8., 'Orbit method dec does not return the correct value as Quantity'
    assert numpy.fabs(o.ll().to(units.deg).value-oc.ll()) < 10.**-8., 'Orbit method ll does not return the correct value as Quantity'
    assert numpy.fabs(o.bb().to(units.deg).value-oc.bb()) < 10.**-8., 'Orbit method bb does not return the correct value as Quantity'
    assert numpy.fabs(o.dist().to(units.kpc).value-oc.dist()) < 10.**-8., 'Orbit method dist does not return the correct value as Quantity'
    assert numpy.fabs(o.pmra().to(units.mas/units.yr).value-oc.pmra()) < 10.**-8., 'Orbit method pmra does not return the correct value as Quantity'
    assert numpy.fabs(o.pmdec().to(units.mas/units.yr).value-oc.pmdec()) < 10.**-8., 'Orbit method pmdec does not return the correct value as Quantity'
    assert numpy.fabs(o.pmll().to(units.mas/units.yr).value-oc.pmll()) < 10.**-8., 'Orbit method pmll does not return the correct value as Quantity'
    assert numpy.fabs(o.pmbb().to(units.mas/units.yr).value-oc.pmbb()) < 10.**-8., 'Orbit method pmbb does not return the correct value as Quantity'
    assert numpy.fabs(o.vlos().to(units.km/units.s).value-oc.vlos()) < 10.**-8., 'Orbit method vlos does not return the correct value as Quantity'
    assert numpy.fabs(o.vra().to(units.km/units.s).value-oc.vra()) < 10.**-8., 'Orbit method vra does not return the correct value as Quantity'
    assert numpy.fabs(o.vdec().to(units.km/units.s).value-oc.vdec()) < 10.**-8., 'Orbit method vdec does not return the correct value as Quantity'
    assert numpy.fabs(o.vll().to(units.km/units.s).value-oc.vll()) < 10.**-8., 'Orbit method vll does not return the correct value as Quantity'
    assert numpy.fabs(o.vbb().to(units.km/units.s).value-oc.vbb()) < 10.**-8., 'Orbit method vbb does not return the correct value as Quantity'
    assert numpy.fabs(o.helioX().to(units.kpc).value-oc.helioX()) < 10.**-8., 'Orbit method helioX does not return the correct value as Quantity'
    assert numpy.fabs(o.helioY().to(units.kpc).value-oc.helioY()) < 10.**-8., 'Orbit method helioY does not return the correct value as Quantity'
    assert numpy.fabs(o.helioZ().to(units.kpc).value-oc.helioZ()) < 10.**-8., 'Orbit method helioZ does not return the correct value as Quantity'
    assert numpy.fabs(o.U().to(units.km/units.s).value-oc.U()) < 10.**-8., 'Orbit method U does not return the correct value as Quantity'
    assert numpy.fabs(o.V().to(units.km/units.s).value-oc.V()) < 10.**-8., 'Orbit method V does not return the correct value as Quantity'
    assert numpy.fabs(o.W().to(units.km/units.s).value-oc.W()) < 10.**-8., 'Orbit method W does not return the correct value as Quantity'
    return None

def test_integrate_timeAsQuantity():
    from galpy.orbit import Orbit
    from galpy.potential import MWPotential
    from galpy.util import bovy_conversion
    import copy
    ro, vo= 8., 200.
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              500.*units.pc,-12.*units.km/units.s,45.*units.deg],
             ro=ro,vo=vo)
    oc= o()
    ts_nounits= numpy.linspace(0.,1.,1001)
    ts= units.Quantity(copy.copy(ts_nounits),unit=units.Gyr)
    ts_nounits/= bovy_conversion.time_in_Gyr(vo,ro)
    # Integrate both with Quantity time and with unitless time
    o.integrate(ts,MWPotential)
    oc.integrate(ts_nounits,MWPotential)
    assert numpy.all(numpy.fabs(o.x(ts)-oc.x(ts_nounits)).value < 10.**-8.), 'Orbit integrated with times specified as Quantity does not agree with Orbit integrated with time specified as array'
    assert numpy.all(numpy.fabs(o.y(ts)-oc.y(ts_nounits)).value < 10.**-8.), 'Orbit integrated with times specified as Quantity does not agree with Orbit integrated with time specified as array'
    assert numpy.all(numpy.fabs(o.z(ts)-oc.z(ts_nounits)).value < 10.**-8.), 'Orbit integrated with times specified as Quantity does not agree with Orbit integrated with time specified as array'
    assert numpy.all(numpy.fabs(o.vx(ts)-oc.vx(ts_nounits)).value < 10.**-8.), 'Orbit integrated with times specified as Quantity does not agree with Orbit integrated with time specified as array'
    assert numpy.all(numpy.fabs(o.vy(ts)-oc.vy(ts_nounits)).value < 10.**-8.), 'Orbit integrated with times specified as Quantity does not agree with Orbit integrated with time specified as array'
    assert numpy.all(numpy.fabs(o.vz(ts)-oc.vz(ts_nounits)).value < 10.**-8.), 'Orbit integrated with times specified as Quantity does not agree with Orbit integrated with time specified as array'
    return None

def test_integrate_timeAsQuantity_Myr():
    from galpy.orbit import Orbit
    from galpy.potential import MWPotential
    from galpy.util import bovy_conversion
    import copy
    ro, vo= 8., 200.
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              500.*units.pc,-12.*units.km/units.s,45.*units.deg],
             ro=ro,vo=vo)
    oc= o()
    ts_nounits= numpy.linspace(0.,1000.,1001)
    ts= units.Quantity(copy.copy(ts_nounits),unit=units.Myr)
    ts_nounits/= bovy_conversion.time_in_Gyr(vo,ro)*1000.
    # Integrate both with Quantity time and with unitless time
    o.integrate(ts,MWPotential)
    oc.integrate(ts_nounits,MWPotential)
    assert numpy.all(numpy.fabs(o.x(ts)-oc.x(ts_nounits)).value < 10.**-8.), 'Orbit integrated with times specified as Quantity does not agree with Orbit integrated with time specified as array'
    assert numpy.all(numpy.fabs(o.y(ts)-oc.y(ts_nounits)).value < 10.**-8.), 'Orbit integrated with times specified as Quantity does not agree with Orbit integrated with time specified as array'
    assert numpy.all(numpy.fabs(o.z(ts)-oc.z(ts_nounits)).value < 10.**-8.), 'Orbit integrated with times specified as Quantity does not agree with Orbit integrated with time specified as array'
    assert numpy.all(numpy.fabs(o.vx(ts)-oc.vx(ts_nounits)).value < 10.**-8.), 'Orbit integrated with times specified as Quantity does not agree with Orbit integrated with time specified as array'
    assert numpy.all(numpy.fabs(o.vy(ts)-oc.vy(ts_nounits)).value < 10.**-8.), 'Orbit integrated with times specified as Quantity does not agree with Orbit integrated with time specified as array'
    assert numpy.all(numpy.fabs(o.vz(ts)-oc.vz(ts_nounits)).value < 10.**-8.), 'Orbit integrated with times specified as Quantity does not agree with Orbit integrated with time specified as array'
    return None

def test_integrate_dxdv_timeAsQuantity():
    from galpy.orbit import Orbit
    from galpy.potential import MWPotential
    from galpy.util import bovy_conversion
    import copy
    ro, vo= 8., 200.
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              45.*units.deg],
             ro=ro,vo=vo)
    oc= o()
    ts_nounits= numpy.linspace(0.,1.,1001)
    ts= units.Quantity(copy.copy(ts_nounits),unit=units.Gyr)
    ts_nounits/= bovy_conversion.time_in_Gyr(vo,ro)
    # Integrate both with Quantity time and with unitless time
    o.integrate_dxdv([1.,0.3,0.4,0.2],ts,MWPotential,
                     rectIn=True,rectOut=True)
    oc.integrate_dxdv([1.,0.3,0.4,0.2],ts_nounits,MWPotential,
                      rectIn=True,rectOut=True)
    dx= o.getOrbit_dxdv()
    dxc= oc.getOrbit_dxdv()
    assert numpy.all(numpy.fabs(dx-dxc) < 10.**-8.), 'Orbit integrated_dxdv with times specified as Quantity does not agree with Orbit integrated_dxdv with time specified as array'
    return None

def test_integrate_dxdv_timeAsQuantity_Myr():
    from galpy.orbit import Orbit
    from galpy.potential import MWPotential
    from galpy.util import bovy_conversion
    import copy
    ro, vo= 8., 200.
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              45.*units.deg],
             ro=ro,vo=vo)
    oc= o()
    ts_nounits= numpy.linspace(0.,1.,1001)
    ts= units.Quantity(copy.copy(ts_nounits),unit=units.Myr)
    ts_nounits/= bovy_conversion.time_in_Gyr(vo,ro)*1000.
    # Integrate both with Quantity time and with unitless time
    o.integrate_dxdv([1.,0.3,0.4,0.2],ts,MWPotential,
                     rectIn=True,rectOut=True)
    oc.integrate_dxdv([1.,0.3,0.4,0.2],ts_nounits,MWPotential,
                      rectIn=True,rectOut=True)
    dx= o.getOrbit_dxdv()
    dxc= oc.getOrbit_dxdv()
    assert numpy.all(numpy.fabs(dx-dxc) < 10.**-8.), 'Orbit integrated_dxdv with times specified as Quantity does not agree with Orbit integrated_dxdv with time specified as array'
    return None

def test_change_ro_config():
    from galpy.orbit import Orbit
    from galpy.util import config
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              45.*units.deg])
    assert numpy.fabs(o._ro-8.) < 10.**-10., 'Default ro value not as expected'
    assert numpy.fabs(o._orb._ro-8.) < 10.**-10., 'Default ro value not as expected'
    # Change value
    newro= 9.
    config.set_ro(newro)
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              45.*units.deg])
    assert numpy.fabs(o._ro-newro) < 10.**-10., 'Default ro value not as expected'
    assert numpy.fabs(o._orb._ro-newro) < 10.**-10., 'Default ro value not as expected'
    # Change value as Quantity
    newro= 9.*units.kpc
    config.set_ro(newro)
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              45.*units.deg])
    assert numpy.fabs(o._ro-newro.value) < 10.**-10., 'Default ro value not as expected'
    assert numpy.fabs(o._orb._ro-newro.value) < 10.**-10., 'Default ro value not as expected'
    return None

def test_change_vo_config():
    from galpy.orbit import Orbit
    from galpy.util import config
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              45.*units.deg])
    assert numpy.fabs(o._vo-220.) < 10.**-10., 'Default ro value not as expected'
    assert numpy.fabs(o._orb._vo-220.) < 10.**-10., 'Default ro value not as expected'
    # Change value
    newvo= 250.
    config.set_vo(newvo)
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              45.*units.deg])
    assert numpy.fabs(o._vo-newvo) < 10.**-10., 'Default ro value not as expected'
    assert numpy.fabs(o._orb._vo-newvo) < 10.**-10., 'Default ro value not as expected'
    # Change value as Quantity
    newvo= 250.*units.km/units.s
    config.set_vo(newvo)
    o= Orbit([10.*units.kpc,-20.*units.km/units.s,210.*units.km/units.s,
              45.*units.deg])
    assert numpy.fabs(o._vo-newvo.value) < 10.**-10., 'Default ro value not as expected'
    assert numpy.fabs(o._orb._vo-newvo.value) < 10.**-10., 'Default ro value not as expected'
    return None

def test_potential_method_returntype():
    from galpy.potential import PlummerPotential
    pot= PlummerPotential(normalize=True,ro=8.,vo=220.)
    assert isinstance(pot(1.1,0.1),units.Quantity), 'Potential method __call__ does not return Quantity when it should'
    assert isinstance(pot.Rforce(1.1,0.1),units.Quantity), 'Potential method Rforce does not return Quantity when it should'
    assert isinstance(pot.zforce(1.1,0.1),units.Quantity), 'Potential method zforce does not return Quantity when it should'
    assert isinstance(pot.phiforce(1.1,0.1),units.Quantity), 'Potential method phiforce does not return Quantity when it should'
    assert isinstance(pot.dens(1.1,0.1),units.Quantity), 'Potential method dens does not return Quantity when it should'
    assert isinstance(pot.mass(1.1,0.1),units.Quantity), 'Potential method mass does not return Quantity when it should'
    assert isinstance(pot.R2deriv(1.1,0.1),units.Quantity), 'Potential method R2deriv does not return Quantity when it should'
    assert isinstance(pot.z2deriv(1.1,0.1),units.Quantity), 'Potential method z2deriv does not return Quantity when it should'
    assert isinstance(pot.Rzderiv(1.1,0.1),units.Quantity), 'Potential method Rzderiv does not return Quantity when it should'
    assert isinstance(pot.Rphideriv(1.1,0.1),units.Quantity), 'Potential method Rphideriv does not return Quantity when it should'
    assert isinstance(pot.phi2deriv(1.1,0.1),units.Quantity), 'Potential method phi2deriv does not return Quantity when it should'
    assert isinstance(pot.vcirc(1.1),units.Quantity), 'Potential method vcirc does not return Quantity when it should'
    assert isinstance(pot.dvcircdR(1.1),units.Quantity), 'Potential method dvcircdR does not return Quantity when it should'
    assert isinstance(pot.omegac(1.1),units.Quantity), 'Potential method omegac does not return Quantity when it should'
    assert isinstance(pot.epifreq(1.1),units.Quantity), 'Potential method epifreq does not return Quantity when it should'
    assert isinstance(pot.verticalfreq(1.1),units.Quantity), 'Potential method verticalfreq does not return Quantity when it should'
    assert pot.lindbladR(0.9) is None, 'Potential method lindbladR does not return None, even when it should return a Quantity, when it should'
    assert isinstance(pot.lindbladR(0.9,m='corot'),units.Quantity), 'Potential method lindbladR does not return Quantity when it should'
    assert isinstance(pot.vesc(1.3),units.Quantity), 'Potential method vesc does not return Quantity when it should'
    assert isinstance(pot.rl(1.3),units.Quantity), 'Potential method rl does not return Quantity when it should'
    assert isinstance(pot.vterm(45.),units.Quantity), 'Potential method vterm does not return Quantity when it should'
    return None

def test_planarPotential_method_returntype():
    from galpy.potential import PlummerPotential
    pot= PlummerPotential(normalize=True,ro=8.,vo=220.).toPlanar()
    assert isinstance(pot(1.1),units.Quantity), 'Potential method __call__ does not return Quantity when it should'
    assert isinstance(pot.Rforce(1.1),units.Quantity), 'Potential method Rforce does not return Quantity when it should'
    assert isinstance(pot.phiforce(1.1),units.Quantity), 'Potential method phiforce does not return Quantity when it should'
    assert isinstance(pot.R2deriv(1.1),units.Quantity), 'Potential method R2deriv does not return Quantity when it should'
    assert isinstance(pot.Rphideriv(1.1),units.Quantity), 'Potential method Rphideriv does not return Quantity when it should'
    assert isinstance(pot.phi2deriv(1.1),units.Quantity), 'Potential method phi2deriv does not return Quantity when it should'
    assert isinstance(pot.vcirc(1.1),units.Quantity), 'Potential method vcirc does not return Quantity when it should'
    assert isinstance(pot.omegac(1.1),units.Quantity), 'Potential method omegac does not return Quantity when it should'
    assert isinstance(pot.epifreq(1.1),units.Quantity), 'Potential method epifreq does not return Quantity when it should'
    assert pot.lindbladR(0.9) is None, 'Potential method lindbladR does not return None, even when it should return a Quantity, when it should'
    assert isinstance(pot.lindbladR(0.9,m='corot'),units.Quantity), 'Potential method lindbladR does not return Quantity when it should'
    assert isinstance(pot.vesc(1.3),units.Quantity), 'Potential method vesc does not return Quantity when it should'
    return None

def test_linearPotential_method_returntype():
    from galpy.potential import PlummerPotential
    pot= PlummerPotential(normalize=True,ro=8.,vo=220.).toVertical(1.1)
    assert isinstance(pot(1.1),units.Quantity), 'Potential method __call__ does not return Quantity when it should'
    assert isinstance(pot.force(1.1),units.Quantity), 'Potential method Rforce does not return Quantity when it should'
    return None

def test_potential_method_returnunit():
    from galpy.potential import PlummerPotential
    pot= PlummerPotential(normalize=True,ro=8.,vo=220.)
    try:
        pot(1.1,0.1).to(units.km**2/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method __call__ does not return Quantity with the right units')
    try:
        pot.Rforce(1.1,0.1).to(units.km/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method Rforce does not return Quantity with the right units')
    try:
        pot.zforce(1.1,0.1).to(units.km/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method zforce does not return Quantity with the right units')
    try:
        pot.phiforce(1.1,0.1).to(units.km/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method phiforce does not return Quantity with the right units')
    try:
        pot.dens(1.1,0.1).to(units.kg/units.m**3)
    except units.UnitConversionError:
        raise AssertionError('Potential method dens does not return Quantity with the right units')
    try:
        pot.mass(1.1,0.1).to(units.kg)
    except units.UnitConversionError:
        raise AssertionError('Potential method mass does not return Quantity with the right units')
    try:
        pot.R2deriv(1.1,0.1).to(1/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method R2deriv does not return Quantity with the right units')
    try:
        pot.z2deriv(1.1,0.1).to(1/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method z2deriv does not return Quantity with the right units')
    try:
        pot.Rzderiv(1.1,0.1).to(1/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method Rzderiv does not return Quantity with the right units')
    try:
        pot.phi2deriv(1.1,0.1).to(1/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method phi2deriv does not return Quantity with the right units')
    try:
        pot.Rphideriv(1.1,0.1).to(1/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method Rphideriv does not return Quantity with the right units')
    try:
        pot.vcirc(1.1).to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential method vcirc does not return Quantity with the right units')
    try:
        pot.dvcircdR(1.1).to(1./units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential method dvcircdR does not return Quantity with the right units')
    try:
        pot.omegac(1.1).to(1./units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential method omegac does not return Quantity with the right units')
    try:
        pot.epifreq(1.1).to(1./units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential method epifreq does not return Quantity with the right units')
    try:
        pot.verticalfreq(1.1).to(1./units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential method verticalfreq does not return Quantity with the right units')
    try:
        pot.lindbladR(0.9,m='corot').to(units.km)
    except units.UnitConversionError:
        raise AssertionError('Potential method lindbladR does not return Quantity with the right units')
    try:
        pot.vesc(1.3).to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential method vesc does not return Quantity with the right units')
    try:
        pot.rl(1.3).to(units.km)
    except units.UnitConversionError:
        raise AssertionError('Potential method rl does not return Quantity with the right units')
    try:
        pot.vterm(45.).to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential method vter does not return Quantity with the right units')
    return None

def test_planarPotential_method_returnunit():
    from galpy.potential import PlummerPotential
    pot= PlummerPotential(normalize=True,ro=8.,vo=220.).toPlanar()
    try:
        pot(1.1).to(units.km**2/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method __call__ does not return Quantity with the right units')
    try:
        pot.Rforce(1.1).to(units.km/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method Rforce does not return Quantity with the right units')
    try:
        pot.phiforce(1.1).to(units.km/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method phiforce does not return Quantity with the right units')
    try:
        pot.R2deriv(1.1).to(1/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method R2deriv does not return Quantity with the right units')
    try:
        pot.phi2deriv(1.1).to(1/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method phi2deriv does not return Quantity with the right units')
    try:
        pot.Rphideriv(1.1).to(1/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method Rphideriv does not return Quantity with the right units')
    try:
        pot.vcirc(1.1).to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential method vcirc does not return Quantity with the right units')
    try:
        pot.omegac(1.1).to(1./units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential method omegac does not return Quantity with the right units')
    try:
        pot.epifreq(1.1).to(1./units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential method epifreq does not return Quantity with the right units')
    try:
        pot.lindbladR(0.9,m='corot').to(units.km)
    except units.UnitConversionError:
        raise AssertionError('Potential method lindbladR does not return Quantity with the right units')
    try:
        pot.vesc(1.3).to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential method vesc does not return Quantity with the right units')
    return None

def test_linearPotential_method_returnunit():
    from galpy.potential import PlummerPotential
    pot= PlummerPotential(normalize=True,ro=8.,vo=220.).toVertical(1.1)
    try:
        pot(1.1).to(units.km**2/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method __call__ does not return Quantity with the right units')
    try:
        pot.force(1.1).to(units.km/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential method force does not return Quantity with the right units')
    return None

def test_potential_method_value():
    from galpy.potential import PlummerPotential
    from galpy.util import bovy_conversion
    ro, vo= 8., 220.
    pot= PlummerPotential(normalize=True,ro=ro,vo=vo)
    potu= PlummerPotential(normalize=True)
    assert numpy.fabs(pot(1.1,0.1).to(units.km**2/units.s**2).value-potu(1.1,0.1)*vo**2.) < 10.**-8., 'Potential method __call__ does not return the correct value as Quantity'
    assert numpy.fabs(pot.Rforce(1.1,0.1).to(units.km/units.s**2).value*10.**13.-potu.Rforce(1.1,0.1)*bovy_conversion.force_in_10m13kms2(vo,ro)) < 10.**-4., 'Potential method Rforce does not return the correct value as Quantity'
    assert numpy.fabs(pot.zforce(1.1,0.1).to(units.km/units.s**2).value*10.**13.-potu.zforce(1.1,0.1)*bovy_conversion.force_in_10m13kms2(vo,ro)) < 10.**-4., 'Potential method zforce does not return the correct value as Quantity'
    assert numpy.fabs(pot.phiforce(1.1,0.1).to(units.km/units.s**2).value*10.**13.-potu.phiforce(1.1,0.1)*bovy_conversion.force_in_10m13kms2(vo,ro)) < 10.**-4., 'Potential method phiforce does not return the correct value as Quantity'
    assert numpy.fabs(pot.dens(1.1,0.1).to(units.Msun/units.pc**3).value-potu.dens(1.1,0.1)*bovy_conversion.dens_in_msolpc3(vo,ro)) < 10.**-8., 'Potential method dens does not return the correct value as Quantity'
    assert numpy.fabs(pot.mass(1.1,0.1).to(units.Msun).value/10.**10.-potu.mass(1.1,0.1)*bovy_conversion.mass_in_1010msol(vo,ro)) < 10.**-8., 'Potential method mass does not return the correct value as Quantity'
    assert numpy.fabs(pot.R2deriv(1.1,0.1).to(units.km**2/units.s**2./units.kpc**2).value-potu.R2deriv(1.1,0.1)*vo**2./ro**2.) < 10.**-8., 'Potential method R2deriv does not return the correct value as Quantity'
    assert numpy.fabs(pot.z2deriv(1.1,0.1).to(units.km**2/units.s**2./units.kpc**2).value-potu.z2deriv(1.1,0.1)*vo**2./ro**2.) < 10.**-8., 'Potential method z2deriv does not return the correct value as Quantity'
    assert numpy.fabs(pot.Rzderiv(1.1,0.1).to(units.km**2/units.s**2./units.kpc**2).value-potu.Rzderiv(1.1,0.1)*vo**2./ro**2.) < 10.**-8., 'Potential method Rzderiv does not return the correct value as Quantity'
    assert numpy.fabs(pot.Rphideriv(1.1,0.1).to(units.km**2/units.s**2./units.kpc**2).value-potu.Rphideriv(1.1,0.1)*vo**2./ro**2.) < 10.**-8., 'Potential method Rphideriv does not return the correct value as Quantity'
    assert numpy.fabs(pot.phi2deriv(1.1,0.1).to(units.km**2/units.s**2./units.kpc**2).value-potu.phi2deriv(1.1,0.1)*vo**2./ro**2.) < 10.**-8., 'Potential method phi2deriv does not return the correct value as Quantity'
    assert numpy.fabs(pot.vcirc(1.1).to(units.km/units.s).value-potu.vcirc(1.1)*vo) < 10.**-8., 'Potential method vcirc does not return the correct value as Quantity'
    assert numpy.fabs(pot.dvcircdR(1.1).to(units.km/units.s/units.kpc).value-potu.dvcircdR(1.1)*vo/ro) < 10.**-8., 'Potential method dvcircdR does not return the correct value as Quantity'
    assert numpy.fabs(pot.omegac(1.1).to(units.km/units.s/units.kpc).value-potu.omegac(1.1)*vo/ro) < 10.**-8., 'Potential method omegac does not return the correct value as Quantity'
    assert numpy.fabs(pot.epifreq(1.1).to(units.km/units.s/units.kpc).value-potu.epifreq(1.1)*vo/ro) < 10.**-8., 'Potential method epifreq does not return the correct value as Quantity'
    assert numpy.fabs(pot.verticalfreq(1.1).to(units.km/units.s/units.kpc).value-potu.verticalfreq(1.1)*vo/ro) < 10.**-8., 'Potential method verticalfreq does not return the correct value as Quantity'
    assert numpy.fabs(pot.lindbladR(0.9,m='corot').to(units.kpc).value-potu.lindbladR(0.9,m='corot')*ro) < 10.**-8., 'Potential method lindbladR does not return the correct value as Quantity'
    assert numpy.fabs(pot.vesc(1.1).to(units.km/units.s).value-potu.vesc(1.1)*vo) < 10.**-8., 'Potential method vesc does not return the correct value as Quantity'
    assert numpy.fabs(pot.rl(1.1).to(units.kpc).value-potu.rl(1.1)*ro) < 10.**-8., 'Potential method rl does not return the correct value as Quantity'
    assert numpy.fabs(pot.vterm(45.).to(units.km/units.s).value-potu.vterm(45.)*vo) < 10.**-8., 'Potential method vterm does not return the correct value as Quantity'
    return None

def test_planarPotential_method_value():
    from galpy.potential import PlummerPotential
    from galpy.util import bovy_conversion
    ro, vo= 8., 220.
    pot= PlummerPotential(normalize=True,ro=ro,vo=vo).toPlanar()
    potu= PlummerPotential(normalize=True).toPlanar()
    assert numpy.fabs(pot(1.1).to(units.km**2/units.s**2).value-potu(1.1)*vo**2.) < 10.**-8., 'Potential method __call__ does not return the correct value as Quantity'
    assert numpy.fabs(pot.Rforce(1.1).to(units.km/units.s**2).value*10.**13.-potu.Rforce(1.1)*bovy_conversion.force_in_10m13kms2(vo,ro)) < 10.**-4., 'Potential method Rforce does not return the correct value as Quantity'
    assert numpy.fabs(pot.phiforce(1.1).to(units.km/units.s**2).value*10.**13.-potu.phiforce(1.1)*bovy_conversion.force_in_10m13kms2(vo,ro)) < 10.**-4., 'Potential method phiforce does not return the correct value as Quantity'
    assert numpy.fabs(pot.R2deriv(1.1).to(units.km**2/units.s**2./units.kpc**2).value-potu.R2deriv(1.1)*vo**2./ro**2.) < 10.**-8., 'Potential method R2deriv does not return the correct value as Quantity'
    assert numpy.fabs(pot.Rphideriv(1.1).to(units.km**2/units.s**2./units.kpc**2).value-potu.Rphideriv(1.1)*vo**2./ro**2.) < 10.**-8., 'Potential method Rphideriv does not return the correct value as Quantity'
    assert numpy.fabs(pot.phi2deriv(1.1).to(units.km**2/units.s**2./units.kpc**2).value-potu.phi2deriv(1.1)*vo**2./ro**2.) < 10.**-8., 'Potential method phi2deriv does not return the correct value as Quantity'
    assert numpy.fabs(pot.vcirc(1.1).to(units.km/units.s).value-potu.vcirc(1.1)*vo) < 10.**-8., 'Potential method vcirc does not return the correct value as Quantity'
    assert numpy.fabs(pot.omegac(1.1).to(units.km/units.s/units.kpc).value-potu.omegac(1.1)*vo/ro) < 10.**-8., 'Potential method omegac does not return the correct value as Quantity'
    assert numpy.fabs(pot.epifreq(1.1).to(units.km/units.s/units.kpc).value-potu.epifreq(1.1)*vo/ro) < 10.**-8., 'Potential method epifreq does not return the correct value as Quantity'
    assert numpy.fabs(pot.vesc(1.1).to(units.km/units.s).value-potu.vesc(1.1)*vo) < 10.**-8., 'Potential method vesc does not return the correct value as Quantity'
    return None

def test_linearPotential_method_value():
    from galpy.potential import PlummerPotential
    from galpy.util import bovy_conversion
    ro, vo= 8., 220.
    pot= PlummerPotential(normalize=True,ro=ro,vo=vo).toVertical(1.1)
    potu= PlummerPotential(normalize=True).toVertical(1.1)
    assert numpy.fabs(pot(1.1).to(units.km**2/units.s**2).value-potu(1.1)*vo**2.) < 10.**-8., 'Potential method __call__ does not return the correct value as Quantity'
    assert numpy.fabs(pot.force(1.1).to(units.km/units.s**2).value*10.**13.-potu.force(1.1)*bovy_conversion.force_in_10m13kms2(vo,ro)) < 10.**-4., 'Potential method force does not return the correct value as Quantity'
    return None

def test_potential_function_returntype():
    from galpy.potential import PlummerPotential
    from galpy import potential
    pot= [PlummerPotential(normalize=True,ro=8.,vo=220.)]
    assert isinstance(potential.evaluatePotentials(pot,1.1,0.1),units.Quantity), 'Potential function __call__ does not return Quantity when it should'
    assert isinstance(potential.evaluateRforces(pot,1.1,0.1),units.Quantity), 'Potential function Rforce does not return Quantity when it should'
    assert isinstance(potential.evaluatezforces(pot,1.1,0.1),units.Quantity), 'Potential function zforce does not return Quantity when it should'
    assert isinstance(potential.evaluatephiforces(pot,1.1,0.1),units.Quantity), 'Potential function phiforce does not return Quantity when it should'
    assert isinstance(potential.evaluateDensities(pot,1.1,0.1),units.Quantity), 'Potential function dens does not return Quantity when it should'
    assert isinstance(potential.evaluateR2derivs(pot,1.1,0.1),units.Quantity), 'Potential function R2deriv does not return Quantity when it should'
    assert isinstance(potential.evaluatez2derivs(pot,1.1,0.1),units.Quantity), 'Potential function z2deriv does not return Quantity when it should'
    assert isinstance(potential.evaluateRzderivs(pot,1.1,0.1),units.Quantity), 'Potential function Rzderiv does not return Quantity when it should'
    assert isinstance(potential.vcirc(pot,1.1),units.Quantity), 'Potential function vcirc does not return Quantity when it should'
    assert isinstance(potential.dvcircdR(pot,1.1),units.Quantity), 'Potential function dvcircdR does not return Quantity when it should'
    assert isinstance(potential.omegac(pot,1.1),units.Quantity), 'Potential function omegac does not return Quantity when it should'
    assert isinstance(potential.epifreq(pot,1.1),units.Quantity), 'Potential function epifreq does not return Quantity when it should'
    assert isinstance(potential.verticalfreq(pot,1.1),units.Quantity), 'Potential function verticalfreq does not return Quantity when it should'
    assert potential.lindbladR(pot,0.9) is None, 'Potential function lindbladR does not return None, even when it should return a Quantity, when it should'
    assert isinstance(potential.lindbladR(pot,0.9,m='corot'),units.Quantity), 'Potential function lindbladR does not return Quantity when it should'
    assert isinstance(potential.vesc(pot,1.3),units.Quantity), 'Potential function vesc does not return Quantity when it should'
    assert isinstance(potential.rl(pot,1.3),units.Quantity), 'Potential function rl does not return Quantity when it should'
    assert isinstance(potential.vterm(pot,45.),units.Quantity), 'Potential function vterm does not return Quantity when it should'
    return None

def test_planarPotential_function_returntype():
    from galpy.potential import PlummerPotential
    from galpy import potential
    pot= [PlummerPotential(normalize=True,ro=8.,vo=220.).toPlanar()]
    assert isinstance(potential.evaluateplanarPotentials(pot,1.1),units.Quantity), 'Potential function __call__ does not return Quantity when it should'
    assert isinstance(potential.evaluateplanarRforces(pot,1.1),units.Quantity), 'Potential function Rforce does not return Quantity when it should'
    assert isinstance(potential.evaluateplanarphiforces(pot,1.1),units.Quantity), 'Potential function phiforce does not return Quantity when it should'
    assert isinstance(potential.evaluateplanarR2derivs(pot,1.1),units.Quantity), 'Potential function R2deriv does not return Quantity when it should'
    assert isinstance(potential.vcirc(pot,1.1),units.Quantity), 'Potential function vcirc does not return Quantity when it should'
    assert isinstance(potential.omegac(pot,1.1),units.Quantity), 'Potential function omegac does not return Quantity when it should'
    assert isinstance(potential.epifreq(pot,1.1),units.Quantity), 'Potential function epifreq does not return Quantity when it should'
    assert potential.lindbladR(pot,0.9) is None, 'Potential function lindbladR does not return None, even when it should return a Quantity, when it should'
    assert isinstance(potential.lindbladR(pot,0.9,m='corot'),units.Quantity), 'Potential function lindbladR does not return Quantity when it should'
    assert isinstance(potential.vesc(pot,1.3),units.Quantity), 'Potential function vesc does not return Quantity when it should'
    return None

def test_linearPotential_function_returntype():
    from galpy.potential import PlummerPotential
    from galpy import potential
    pot= [PlummerPotential(normalize=True,ro=8.,vo=220.).toVertical(1.1)]
    assert isinstance(potential.evaluatelinearPotentials(pot,1.1),units.Quantity), 'Potential function __call__ does not return Quantity when it should'
    assert isinstance(potential.evaluatelinearForces(pot,1.1),units.Quantity), 'Potential function Rforce does not return Quantity when it should'
    return None

def test_potential_function_returnunit():
    from galpy.potential import PlummerPotential
    from galpy import potential
    pot= [PlummerPotential(normalize=True,ro=8.,vo=220.)]
    try:
        potential.evaluatePotentials(pot,1.1,0.1).to(units.km**2/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential function __call__ does not return Quantity with the right units')
    try:
        potential.evaluateRforces(pot,1.1,0.1).to(units.km/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential function Rforce does not return Quantity with the right units')
    try:
        potential.evaluatezforces(pot,1.1,0.1).to(units.km/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential function zforce does not return Quantity with the right units')
    try:
        potential.evaluatephiforces(pot,1.1,0.1).to(units.km/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential function phiforce does not return Quantity with the right units')
    try:
        potential.evaluateDensities(pot,1.1,0.1).to(units.kg/units.m**3)
    except units.UnitConversionError:
        raise AssertionError('Potential function dens does not return Quantity with the right units')
    try:
        potential.evaluateR2derivs(pot,1.1,0.1).to(1/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential function R2deriv does not return Quantity with the right units')
    try:
        potential.evaluatez2derivs(pot,1.1,0.1).to(1/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential function z2deriv does not return Quantity with the right units')
    try:
        potential.evaluateRzderivs(pot,1.1,0.1).to(1/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential function Rzderiv does not return Quantity with the right units')
    try:
        potential.vcirc(pot,1.1).to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential function vcirc does not return Quantity with the right units')
    try:
        potential.dvcircdR(pot,1.1).to(1./units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential function dvcircdR does not return Quantity with the right units')
    try:
        potential.omegac(pot,1.1).to(1./units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential function omegac does not return Quantity with the right units')
    try:
        potential.epifreq(pot,1.1).to(1./units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential function epifreq does not return Quantity with the right units')
    try:
        potential.verticalfreq(pot,1.1).to(1./units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential function verticalfreq does not return Quantity with the right units')
    try:
        potential.lindbladR(pot,0.9,m='corot').to(units.km)
    except units.UnitConversionError:
        raise AssertionError('Potential function lindbladR does not return Quantity with the right units')
    try:
        potential.vesc(pot,1.3).to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential function vesc does not return Quantity with the right units')
    try:
        potential.rl(pot,1.3).to(units.km)
    except units.UnitConversionError:
        raise AssertionError('Potential function rl does not return Quantity with the right units')
    try:
        potential.vterm(pot,45.).to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential function vter does not return Quantity with the right units')
    return None

def test_planarPotential_function_returnunit():
    from galpy.potential import PlummerPotential
    from galpy import potential
    pot= [PlummerPotential(normalize=True,ro=8.,vo=220.).toPlanar()]
    try:
        potential.evaluateplanarPotentials(pot,1.1).to(units.km**2/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential function __call__ does not return Quantity with the right units')
    try:
        potential.evaluateplanarRforces(pot,1.1).to(units.km/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential function Rforce does not return Quantity with the right units')
    try:
        potential.evaluateplanarphiforces(pot,1.1).to(units.km/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential function phiforce does not return Quantity with the right units')
    try:
        potential.evaluateplanarR2derivs(pot,1.1).to(1/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential function R2deriv does not return Quantity with the right units')
    try:
        potential.vcirc(pot,1.1).to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential function vcirc does not return Quantity with the right units')
    try:
        potential.omegac(pot,1.1).to(1./units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential function omegac does not return Quantity with the right units')
    try:
        potential.epifreq(pot,1.1).to(1./units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential function epifreq does not return Quantity with the right units')
    try:
        potential.lindbladR(pot,0.9,m='corot').to(units.km)
    except units.UnitConversionError:
        raise AssertionError('Potential function lindbladR does not return Quantity with the right units')
    try:
        potential.vesc(pot,1.3).to(units.km/units.s)
    except units.UnitConversionError:
        raise AssertionError('Potential function vesc does not return Quantity with the right units')
    return None

def test_linearPotential_function_returnunit():
    from galpy.potential import PlummerPotential
    from galpy import potential
    pot= [PlummerPotential(normalize=True,ro=8.,vo=220.).toVertical(1.1)]
    try:
        potential.evaluatelinearPotentials(pot,1.1).to(units.km**2/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential function __call__ does not return Quantity with the right units')
    try:
        potential.evaluatelinearForces(pot,1.1).to(units.km/units.s**2)
    except units.UnitConversionError:
        raise AssertionError('Potential function force does not return Quantity with the right units')
    return None

def test_potential_function_value():
    from galpy.potential import PlummerPotential
    from galpy import potential
    from galpy.util import bovy_conversion
    ro, vo= 8., 220.
    pot= [PlummerPotential(normalize=True,ro=ro,vo=vo)]
    potu= [PlummerPotential(normalize=True)]
    assert numpy.fabs(potential.evaluatePotentials(pot,1.1,0.1).to(units.km**2/units.s**2).value-potential.evaluatePotentials(potu,1.1,0.1)*vo**2.) < 10.**-8., 'Potential function __call__ does not return the correct value as Quantity'
    assert numpy.fabs(potential.evaluateRforces(pot,1.1,0.1).to(units.km/units.s**2).value*10.**13.-potential.evaluateRforces(potu,1.1,0.1)*bovy_conversion.force_in_10m13kms2(vo,ro)) < 10.**-4., 'Potential function Rforce does not return the correct value as Quantity'
    assert numpy.fabs(potential.evaluatezforces(pot,1.1,0.1).to(units.km/units.s**2).value*10.**13.-potential.evaluatezforces(potu,1.1,0.1)*bovy_conversion.force_in_10m13kms2(vo,ro)) < 10.**-4., 'Potential function zforce does not return the correct value as Quantity'
    assert numpy.fabs(potential.evaluatephiforces(pot,1.1,0.1).to(units.km/units.s**2).value*10.**13.-potential.evaluatephiforces(potu,1.1,0.1)*bovy_conversion.force_in_10m13kms2(vo,ro)) < 10.**-4., 'Potential function phiforce does not return the correct value as Quantity'
    assert numpy.fabs(potential.evaluateDensities(pot,1.1,0.1).to(units.Msun/units.pc**3).value-potential.evaluateDensities(potu,1.1,0.1)*bovy_conversion.dens_in_msolpc3(vo,ro)) < 10.**-8., 'Potential function dens does not return the correct value as Quantity'
    assert numpy.fabs(potential.evaluateR2derivs(pot,1.1,0.1).to(units.km**2/units.s**2./units.kpc**2).value-potential.evaluateR2derivs(potu,1.1,0.1)*vo**2./ro**2.) < 10.**-8., 'Potential function R2deriv does not return the correct value as Quantity'
    assert numpy.fabs(potential.evaluatez2derivs(pot,1.1,0.1).to(units.km**2/units.s**2./units.kpc**2).value-potential.evaluatez2derivs(potu,1.1,0.1)*vo**2./ro**2.) < 10.**-8., 'Potential function z2deriv does not return the correct value as Quantity'
    assert numpy.fabs(potential.evaluateRzderivs(pot,1.1,0.1).to(units.km**2/units.s**2./units.kpc**2).value-potential.evaluateRzderivs(potu,1.1,0.1)*vo**2./ro**2.) < 10.**-8., 'Potential function Rzderiv does not return the correct value as Quantity'
    assert numpy.fabs(potential.vcirc(pot,1.1).to(units.km/units.s).value-potential.vcirc(potu,1.1)*vo) < 10.**-8., 'Potential function vcirc does not return the correct value as Quantity'
    assert numpy.fabs(potential.dvcircdR(pot,1.1).to(units.km/units.s/units.kpc).value-potential.dvcircdR(potu,1.1)*vo/ro) < 10.**-8., 'Potential function dvcircdR does not return the correct value as Quantity'
    assert numpy.fabs(potential.omegac(pot,1.1).to(units.km/units.s/units.kpc).value-potential.omegac(potu,1.1)*vo/ro) < 10.**-8., 'Potential function omegac does not return the correct value as Quantity'
    assert numpy.fabs(potential.epifreq(pot,1.1).to(units.km/units.s/units.kpc).value-potential.epifreq(potu,1.1)*vo/ro) < 10.**-8., 'Potential function epifreq does not return the correct value as Quantity'
    assert numpy.fabs(potential.verticalfreq(pot,1.1).to(units.km/units.s/units.kpc).value-potential.verticalfreq(potu,1.1)*vo/ro) < 10.**-8., 'Potential function verticalfreq does not return the correct value as Quantity'
    assert numpy.fabs(potential.lindbladR(pot,0.9,m='corot').to(units.kpc).value-potential.lindbladR(potu,0.9,m='corot')*ro) < 10.**-8., 'Potential function lindbladR does not return the correct value as Quantity'
    assert numpy.fabs(potential.vesc(pot,1.1).to(units.km/units.s).value-potential.vesc(potu,1.1)*vo) < 10.**-8., 'Potential function vesc does not return the correct value as Quantity'
    assert numpy.fabs(potential.rl(pot,1.1).to(units.kpc).value-potential.rl(potu,1.1)*ro) < 10.**-8., 'Potential function rl does not return the correct value as Quantity'
    assert numpy.fabs(potential.vterm(pot,45.).to(units.km/units.s).value-potential.vterm(potu,45.)*vo) < 10.**-8., 'Potential function vterm does not return the correct value as Quantity'
    return None

def test_planarPotential_function_value():
    from galpy.potential import PlummerPotential
    from galpy import potential
    from galpy.util import bovy_conversion
    ro, vo= 8., 220.
    pot= [PlummerPotential(normalize=True,ro=ro,vo=vo).toPlanar()]
    potu= [PlummerPotential(normalize=True).toPlanar()]
    assert numpy.fabs(potential.evaluateplanarPotentials(pot,1.1).to(units.km**2/units.s**2).value-potential.evaluateplanarPotentials(potu,1.1)*vo**2.) < 10.**-8., 'Potential function __call__ does not return the correct value as Quantity'
    assert numpy.fabs(potential.evaluateplanarRforces(pot,1.1).to(units.km/units.s**2).value*10.**13.-potential.evaluateplanarRforces(potu,1.1)*bovy_conversion.force_in_10m13kms2(vo,ro)) < 10.**-4., 'Potential function Rforce does not return the correct value as Quantity'
    assert numpy.fabs(potential.evaluateplanarphiforces(pot,1.1).to(units.km/units.s**2).value*10.**13.-potential.evaluateplanarphiforces(potu,1.1)*bovy_conversion.force_in_10m13kms2(vo,ro)) < 10.**-4., 'Potential function phiforce does not return the correct value as Quantity'
    assert numpy.fabs(potential.evaluateplanarR2derivs(pot,1.1).to(units.km**2/units.s**2./units.kpc**2).value-potential.evaluateplanarR2derivs(potu,1.1)*vo**2./ro**2.) < 10.**-8., 'Potential function R2deriv does not return the correct value as Quantity'
    assert numpy.fabs(potential.vcirc(pot,1.1).to(units.km/units.s).value-potential.vcirc(potu,1.1)*vo) < 10.**-8., 'Potential function vcirc does not return the correct value as Quantity'
    assert numpy.fabs(potential.omegac(pot,1.1).to(units.km/units.s/units.kpc).value-potential.omegac(potu,1.1)*vo/ro) < 10.**-8., 'Potential function omegac does not return the correct value as Quantity'
    assert numpy.fabs(potential.epifreq(pot,1.1).to(units.km/units.s/units.kpc).value-potential.epifreq(potu,1.1)*vo/ro) < 10.**-8., 'Potential function epifreq does not return the correct value as Quantity'
    assert numpy.fabs(potential.vesc(pot,1.1).to(units.km/units.s).value-potential.vesc(potu,1.1)*vo) < 10.**-8., 'Potential function vesc does not return the correct value as Quantity'
    return None

def test_linearPotential_function_value():
    from galpy.potential import PlummerPotential
    from galpy import potential
    from galpy.util import bovy_conversion
    ro, vo= 8., 220.
    pot= [PlummerPotential(normalize=True,ro=ro,vo=vo).toVertical(1.1)]
    potu= [PlummerPotential(normalize=True).toVertical(1.1)]
    assert numpy.fabs(potential.evaluatelinearPotentials(pot,1.1).to(units.km**2/units.s**2).value-potential.evaluatelinearPotentials(potu,1.1)*vo**2.) < 10.**-8., 'Potential function __call__ does not return the correct value as Quantity'
    assert numpy.fabs(potential.evaluatelinearForces(pot,1.1).to(units.km/units.s**2).value*10.**13.-potential.evaluatelinearForces(potu,1.1)*bovy_conversion.force_in_10m13kms2(vo,ro)) < 10.**-4., 'Potential function force does not return the correct value as Quantity'
    return None

def test_potential_method_inputAsQuantity():
    from galpy.potential import PlummerPotential
    ro, vo= 8.*units.kpc, 220.
    pot= PlummerPotential(normalize=True,ro=ro,vo=vo)
    potu= PlummerPotential(normalize=True)
    assert numpy.fabs(pot(1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potu(1.1,0.1)) < 10.**-8., 'Potential method __call__ does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.Rforce(1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potu.Rforce(1.1,0.1)) < 10.**-4., 'Potential method Rforce does not return the correct value when input is Quantity'
    # Few more cases for Rforce
    assert numpy.fabs(pot.Rforce(1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,ro=9.,use_physical=False)-potu.Rforce(1.1*8./9.,0.1*8./9.)) < 10.**-4., 'Potential method Rforce does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.Rforce(1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,vo=230.,use_physical=False)-potu.Rforce(1.1,0.1)) < 10.**-4., 'Potential method Rforce does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.zforce(1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potu.zforce(1.1,0.1)) < 10.**-4., 'Potential method zforce does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.phiforce(1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potu.phiforce(1.1,0.1)) < 10.**-4., 'Potential method phiforce does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.dens(1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potu.dens(1.1,0.1)) < 10.**-8., 'Potential method dens does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.mass(1.1*ro,0.1*ro,use_physical=False)-potu.mass(1.1,0.1)) < 10.**-8., 'Potential method mass does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.R2deriv(1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potu.R2deriv(1.1,0.1)) < 10.**-8., 'Potential method R2deriv does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.z2deriv(1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potu.z2deriv(1.1,0.1)) < 10.**-8., 'Potential method z2deriv does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.Rzderiv(1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potu.Rzderiv(1.1,0.1)) < 10.**-8., 'Potential method Rzderiv does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.Rphideriv(1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potu.Rphideriv(1.1,0.1)) < 10.**-8., 'Potential method Rphideriv does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.phi2deriv(1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potu.phi2deriv(1.1,0.1)) < 10.**-8., 'Potential method phi2deriv does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.vcirc(1.1*ro,use_physical=False)-potu.vcirc(1.1)) < 10.**-8., 'Potential method vcirc does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.dvcircdR(1.1*ro,use_physical=False)-potu.dvcircdR(1.1)) < 10.**-8., 'Potential method dvcircdR does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.omegac(1.1*ro,use_physical=False)-potu.omegac(1.1)) < 10.**-8., 'Potential method omegac does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.epifreq(1.1*ro,use_physical=False)-potu.epifreq(1.1)) < 10.**-8., 'Potential method epifreq does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.verticalfreq(1.1*ro,use_physical=False)-potu.verticalfreq(1.1)) < 10.**-8., 'Potential method verticalfreq does not return the correct value when input is Quantity'
    assert numpy.fabs(pot.vesc(1.1*ro,use_physical=False)-potu.vesc(1.1)) < 10.**-8., 'Potential method vesc does not return the correct value when input is Quantity'
    return None

def test_planarPotential_method_inputAsQuantity():
    from galpy.potential import PlummerPotential
    ro, vo= 8.*units.kpc, 220.
    pot= PlummerPotential(normalize=True,ro=ro,vo=vo).toPlanar()
    potu= PlummerPotential(normalize=True).toPlanar()
    assert numpy.fabs(pot(1.1*ro,use_physical=False)-potu(1.1)) < 10.**-8., 'Potential method __call__ does not return the correct value as Quantity'
    assert numpy.fabs(pot.Rforce(1.1*ro,use_physical=False)-potu.Rforce(1.1)) < 10.**-4., 'Potential method Rforce does not return the correct value as Quantity'
    assert numpy.fabs(pot.phiforce(1.1*ro,use_physical=False)-potu.phiforce(1.1)) < 10.**-4., 'Potential method phiforce does not return the correct value as Quantity'
    assert numpy.fabs(pot.R2deriv(1.1*ro,use_physical=False)-potu.R2deriv(1.1)) < 10.**-8., 'Potential method R2deriv does not return the correct value as Quantity'
    assert numpy.fabs(pot.Rphideriv(1.1*ro,use_physical=False)-potu.Rphideriv(1.1)) < 10.**-8., 'Potential method Rphideriv does not return the correct value as Quantity'
    assert numpy.fabs(pot.phi2deriv(1.1*ro,use_physical=False)-potu.phi2deriv(1.1)) < 10.**-8., 'Potential method phi2deriv does not return the correct value as Quantity'
    assert numpy.fabs(pot.vcirc(1.1*ro,use_physical=False)-potu.vcirc(1.1)) < 10.**-8., 'Potential method vcirc does not return the correct value as Quantity'
    assert numpy.fabs(pot.omegac(1.1*ro,use_physical=False)-potu.omegac(1.1)) < 10.**-8., 'Potential method omegac does not return the correct value as Quantity'
    assert numpy.fabs(pot.epifreq(1.1*ro,use_physical=False)-potu.epifreq(1.1)) < 10.**-8., 'Potential method epifreq does not return the correct value as Quantity'
    assert numpy.fabs(pot.vesc(1.1*ro,use_physical=False)-potu.vesc(1.1)) < 10.**-8., 'Potential method vesc does not return the correct value as Quantity'
    return None

def test_linearPotential_method_inputAsQuantity():
    from galpy.potential import PlummerPotential
    ro, vo= 8.*units.kpc, 220.
    pot= PlummerPotential(normalize=True,ro=ro,vo=vo).toVertical(1.1)
    potu= PlummerPotential(normalize=True).toVertical(1.1)
    assert numpy.fabs(pot(1.1*ro,use_physical=False)-potu(1.1)) < 10.**-8., 'Potential method __call__ does not return the correct value as Quantity'
    assert numpy.fabs(pot.force(1.1*ro,use_physical=False)-potu.force(1.1)) < 10.**-4., 'Potential method force does not return the correct value as Quantity'
    return None

def test_potential_function_inputAsQuantity():
    from galpy.potential import PlummerPotential
    from galpy import potential
    ro, vo= 8.*units.kpc, 220.
    pot= [PlummerPotential(normalize=True,ro=ro,vo=vo)]
    potu= [PlummerPotential(normalize=True)]
    assert numpy.fabs(potential.evaluatePotentials(pot,1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potential.evaluatePotentials(potu,1.1,0.1)) < 10.**-8., 'Potential function __call__ does not return the correct value when input is Quantity'
    assert numpy.fabs(potential.evaluateRforces(pot,1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potential.evaluateRforces(potu,1.1,0.1)) < 10.**-4., 'Potential function Rforce does not return the correct value when input is Quantity'
    assert numpy.fabs(potential.evaluatezforces(pot,1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potential.evaluatezforces(potu,1.1,0.1)) < 10.**-4., 'Potential function zforce does not return the correct value when input is Quantity'
    assert numpy.fabs(potential.evaluatephiforces(pot,1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potential.evaluatephiforces(potu,1.1,0.1)) < 10.**-4., 'Potential function phiforce does not return the correct value when input is Quantity'
    assert numpy.fabs(potential.evaluateDensities(pot,1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potential.evaluateDensities(potu,1.1,0.1)) < 10.**-8., 'Potential function dens does not return the correct value when input is Quantity'
    assert numpy.fabs(potential.evaluateR2derivs(pot,1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potential.evaluateR2derivs(potu,1.1,0.1)) < 10.**-8., 'Potential function R2deriv does not return the correct value when input is Quantity'
    assert numpy.fabs(potential.evaluatez2derivs(pot,1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potential.evaluatez2derivs(potu,1.1,0.1)) < 10.**-8., 'Potential function z2deriv does not return the correct value when input is Quantity'
    assert numpy.fabs(potential.evaluateRzderivs(pot,1.1*ro,0.1*ro,phi=10.*units.deg,t=10.*units.Gyr,use_physical=False)-potential.evaluateRzderivs(potu,1.1,0.1)) < 10.**-8., 'Potential function Rzderiv does not return the correct value when input is Quantity'
    assert numpy.fabs(potential.vcirc(pot,1.1*ro,use_physical=False)-potential.vcirc(potu,1.1)) < 10.**-8., 'Potential function vcirc does not return the correct value when input is Quantity'
    assert numpy.fabs(potential.dvcircdR(pot,1.1*ro,use_physical=False)-potential.dvcircdR(potu,1.1)) < 10.**-8., 'Potential function dvcircdR does not return the correct value when input is Quantity'
    assert numpy.fabs(potential.omegac(pot,1.1*ro,use_physical=False)-potential.omegac(potu,1.1)) < 10.**-8., 'Potential function omegac does not return the correct value when input is Quantity'
    assert numpy.fabs(potential.epifreq(pot,1.1*ro,use_physical=False)-potential.epifreq(potu,1.1)) < 10.**-8., 'Potential function epifreq does not return the correct value when input is Quantity'
    assert numpy.fabs(potential.verticalfreq(pot,1.1*ro,use_physical=False)-potential.verticalfreq(potu,1.1)) < 10.**-8., 'Potential function verticalfreq does not return the correct value when input is Quantity'
    assert numpy.fabs(potential.vesc(pot,1.1*ro,use_physical=False)-potential.vesc(potu,1.1)) < 10.**-8., 'Potential function vesc does not return the correct value when input is Quantity'
    return None

