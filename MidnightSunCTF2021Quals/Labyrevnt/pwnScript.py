from pwn import *
io = remote('labyrevnt-01.play.midnightsunctf.se',29285)
answer = 'a\nB\nI\nk\ns\nN\nP\nZ\nl\nf\nM\nn\nl\nu\nF\nM\nR\nq\nt\nN\nO\nA\nk\nd\nW\nf\nu\nM\nu\nT\nI\nI\nC\nG\nG\nW\nv\nh\nb\nW\nY\nw\nM\nl\nb\nd\nl\nC\nG\nz\nn\nV\nN\nV\nz\nA\ns\nH\nj\ny\nn\nO\nj\nH\nu\nu\nu\nv\nM\nk\nO\nm\nL\nM\nh\nY\nV\ne\nE\nW\nK\nj\nG\nL\nh\nm\nh\nL\nx\ny\nv\nt\nv\nx\np\nz\nG\nC\nW\nu\ni\nb\nx\nD\nh\nG\nz\nE\nm\nA\nf\nk\ne\np\nZ\nD\nI\nN\nx\nd\nH\nT\nQ\nk\nK\nr\ni\nr\nk\nJ\nN\nn\nm\ny\nV\nR\nw\ne\nE\nj\nB\no\nE\nA\nw\ng\nT\nV\nE\nE\nk\nE\nV\nd\nR\nj\nz\nA\nF\nc\nx\nZ\nr\nd\nS\nY\nb\nP\nQ\ns\nt\nu\nI\nL\ns\nI\nj\nO\nS\nW\ng\nL\nL\nL\nX\nv\nk\nC\nA\nQ\nV\ny\nY\nq\nJ\nx\na'
io.send(answer)
print(io.recvline())
print(io.recvline())
print(io.recvline())
