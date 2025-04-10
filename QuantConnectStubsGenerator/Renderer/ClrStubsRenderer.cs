/*
 * QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
 * Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

using System.IO;

namespace QuantConnectStubsGenerator.Renderer
{
    public class ClrStubsRenderer : BaseRenderer
    {
        public ClrStubsRenderer(TextWriter writer) : base(writer)
        {
        }

        public void Render()
        {
            WriteLine($@"
import typing

import System
import System.Reflection


def getPreload() -> bool:
    ...


def setPreload(preloadFlag: bool) -> None:
    ...


def AddReference(name: str) -> System.Reflection.Assembly:
    ...


def GetClrType(type: typing.Type[typing.Any]) -> System.Type:
    ...


def FindAssembly(name: str) -> str:
    ...


def ListAssemblies(verbose: bool) -> typing.List[System.Reflection.Assembly]:
    ...
            ".Trim());
        }
    }
}

