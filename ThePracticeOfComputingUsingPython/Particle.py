# encoding: utf-8

class particle(object):
    def __init__(self,name='',position=(0.0,0.0,0.0),velocity=(0.0,0.0,0.0),spin=0.0):
        self.position = position
        self.velocity = velocity
        self.name = name
        self.spin = spin

    def __str__(self):
        print 'in particle str'
        pos = '(%f:%f:%f)'%(self.position[0],self.position[1],self.position[2])
        vel = '(%f:%f:%f)' % (self.velocity[0], self.velocity[1], self.velocity[2])
        theStr = "%s\n at %s\n with velocity %s\n and spin %f\n"%(self.name,pos,vel,self.spin)
        return  theStr

class massParticle(particle):
    def __init__(self,name='',position=(0.0,0.0,0.0),velocity=(0.0,0.0,0.0),spin=0.0,mass=0.0):
        particle.__init__(self,name,position,velocity,spin)
        self.mass=mass

    def __str__(self):
        print 'in mass str'
        tempStr = particle.__str__(self)
        tempStr = tempStr + 'and mass %f'%(self.mass)
        return tempStr


class chargedParticle(massParticle):
    def __init__(self, name='', position=(0.0, 0.0, 0.0), velocity=(0.0, 0.0, 0.0), spin=0.0, mass=0.0,charge=0.0):
        massParticle.__init__(self, name, position, velocity, spin,mass)
        self.charge = charge

    def __str__(self):
        print 'in charged str'
        tempStr = massParticle.__str__(self)
        tempStr = tempStr + 'and charged %f' % (self.charge)
        return tempStr


def main():
    photon = particle(name='photon',spin=1.0)
    tau = chargedParticle(name='tau',spin=0.5,charge=-1.0,mass=1.777)
    print photon
    print tau
main()



