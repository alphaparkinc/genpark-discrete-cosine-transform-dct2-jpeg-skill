"""MCP stdio server for DCT Engine."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import CosineTransform

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "compute_dct",
                        "description": "Compute orthonormal Type-II Discrete Cosine Transform",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "signal": {"type": "array", "items": {"type": "number"}}
                            },
                            "required": ["signal"]
                        }
                    },
                    {
                        "name": "compute_idct",
                        "description": "Compute Inverse DCT reconstruction",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "coefficients": {"type": "array", "items": {"type": "number"}}
                            },
                            "required": ["coefficients"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "compute_dct":
            sig = args.get("signal", [])
            c = CosineTransform.dct2(sig)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"coefficients": c}}
        elif name == "compute_idct":
            c = args.get("coefficients", [])
            recon = CosineTransform.idct(c)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"signal": recon}}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
