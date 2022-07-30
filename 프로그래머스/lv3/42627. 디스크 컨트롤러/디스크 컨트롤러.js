function solution(jobs) {
    let res = []
    let time = 0
    let controller = []
    jobs = jobs.sort((a,b) => b[0]-a[0] || b[1]-a[1])

    while (jobs.length || controller.length) {
        while (jobs.length && jobs[jobs.length-1][0] <= time) {
            controller.push(jobs.pop())
        }
        if (controller.length) {
            let [request_time, cost] = controller[0]
            let popIdx = 0
            for (idx = 1; idx < controller.length; idx++) {
                if (controller[idx][1] < cost) {
                    [request_time, cost] = controller[idx]
                    popIdx = idx
                }
            }
            controller.splice(popIdx,1)
            res.push(time-request_time+cost)
            time += cost
        } else {
            time = jobs[jobs.length-1][0]
        }
    }
    return Math.floor(res.reduce((acc,cur)=>acc+cur)/res.length)
}