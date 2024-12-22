function solution(grid) {
    const R = grid.length, C = grid[0].length;
    const drc = [[-1,0], [0,1], [1,0], [0,-1]];
    const grf = [];
    for (let r=0; r<R; r++) {
        const row = [];
        for (let c=0; c<C; c++) {
            const cell = [false, false, false, false];
            row.push(cell)
        }
        grf.push(row);
    }
    
    const solve = (r, c, d) => {
        let res = 0;
        while (!grf[r][c][d]) {
            res++;
            grf[r][c][d] = true;
            r = (r + drc[d][0] + R) % R;
            c = (c + drc[d][1] + C) % C;
            if (grid[r][c] === 'L') { d = (d+1)%4; }
            else if (grid[r][c] === 'R') { d = (d+3)%4; }
        }
        return res;
    }
    
    
    const ans = [];
    for (let r=0; r<R; r++) {
        for (let c=0; c<C; c++) {
            for (let d=0; d<4; d++) {
                const cycleLength = solve(r, c, d);
                if (cycleLength > 0) {
                    ans.push(cycleLength);
                }
            }
        }
    }
    return ans.sort((a,b) => a-b)
}