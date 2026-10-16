const API="http://127.0.0.1:8765/api";
export type Feature={id:string;name:string;description:string;category:string;dependencies:string[];implemented:boolean;enabled:boolean;status:string};
export type Job={id:string;kind:string;status:string;message:string;created_at:string;updated_at:string};
export type Metrics={cpu_percent:number;memory_percent:number;memory_used_gb:number;memory_total_gb:number;disk_percent:number;disk_used_gb:number;disk_total_gb:number};
async function req<T>(path:string,init?:RequestInit):Promise<T>{const r=await fetch(API+path,{...init,headers:{"Content-Type":"application/json",...(init?.headers||{})}});if(!r.ok){const b=await r.json().catch(()=>({detail:r.statusText}));throw new Error(b.detail||`Request failed (${r.status})`)}return r.json()}
export const api={
 health:()=>req<{status:string;version:string}>("/health"),
 metrics:()=>req<Metrics>("/system"),
 features:async()=>(await req<{features:Feature[]}>("/features")).features,
 update:async(id:string,enabled:boolean)=>(await req<{feature:Feature}>(`/features/${id}`,{method:"PUT",body:JSON.stringify({enabled})})).feature,
 jobs:async()=>(await req<{jobs:Job[]}>("/jobs")).jobs,
 start:async()=>(await req<{job:Job}>("/jobs/demo",{method:"POST"})).job,
 cancel:async(id:string)=>(await req<{job:Job}>(`/jobs/${id}/cancel`,{method:"POST"})).job
};
